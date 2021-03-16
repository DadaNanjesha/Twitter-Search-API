# Author : Dada Nanjesha GS (dadananjesha@rymec.com)
# Year : 2021
# Copyright: Dada Nanjesha GS

"""
This file contains all the Django REST Framework APIs for search_tweet and TwitterSearchList

This script requires that `twitter` ,`json`, `rest_framework`, `HttpResponse`, `django`, `datetime` be
installed within the Python environment you are running this script in.
"""
import csv
import datetime as dt
import json
from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from twitter import Twitter, OAuth
from .models import TwitterData
from .serializers import TwitterSearchSerializer
from rest_framework import filters

date_format = '%a %b %d %H:%M:%S %z %Y'
application_type = 'application/json'


@api_view(['GET'])
def search_tweet(request):
    """
    API 1 to trigger a twitter search for recent high traffic events. (e.g. #ElectionDay,
    #Elections2020, #TRUMP202s0Landslide, #BidenHarris2020 etc were high traffic
    hashtags during the US Presidential elections 2020).
        a. Trigger search for keyword sent in request
        b. You can use libraries for twitter search
        c. Fetch tweets from twitter and store a normalized and curated version of the tweet
        data.
        d. Architect appropriate database and schema keeping redundancy and query
        simplicity in mind.

    EXAMPLE : http://127.0.0.1:8000/search/?query=TRUMP2020Landslide

    :param request: API request
    :type request: query
    :return: msg
    :rtype: HttpResponse
    :exception: KeyError, ValueError, TypeError, Exception
    """
    result = {}
    load = []
    try:
        query = request.GET.get('query')
        data = search_data(query)
    except (KeyError, ValueError, TypeError) as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return HttpResponse(json.dumps(response_obj), content_type=application_type,
                            status=status.HTTP_400_BAD_REQUEST)
    try:
        data_dict = data['statuses']
        for data in data_dict:
            records = TwitterData()
            records.id = data['id']
            records.text = data['text']
            records.user = data['user']['name']
            records.url = data['user']['url']
            records.lang = data['lang']
            date_time = data['created_at']
            date_field = dt.datetime.strptime(str(date_time), date_format)
            records.created_at = date_field
            records.retweet_count = data['retweet_count']
            records.favorite_count = data['favorite_count']
            if TwitterData.objects.filter(id=data['id']).count() == 0:
                load.append(records)
        TwitterData.objects.bulk_create(load)
        result = {'msg': 'Data loaded successfully'}
        return HttpResponse(json.dumps(result), content_type=application_type, status=status.HTTP_200_OK)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return HttpResponse(json.dumps(response_obj), content_type=application_type,
                            status=status.HTTP_404_NOT_FOUND)


def search_data(query):
    """
    Data returned with dict values
    :param request: query
    :return: data
    :rtype: dict
    """
    t = Twitter(
        auth=OAuth('1365015472345804805-zhFdcYeHZEjxUGqCVNRWRD3OkQR1uW',
                   'KrJqM2dxoyEZDL4p3YIkCGV6mciWp3avVv70LvAiA4poC',
                   '0BO3kvySE1HZYtcAEHhQP3Hnk', '7SuvnCx4ofW0mg7QDW1C50tUzZeZDX2dJRN4xdTCY2iLBz62CA'))
    data = t.search.tweets(q=query)
    u_data = json.dumps(data)
    data = json.loads(u_data)
    return data


class TwitterSearchListPagination(PageNumberPagination):
    """
    TwitterSearchListPagination Class is used to get the Pagination for API

    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class TwitterSearchList(generics.ListCreateAPIView):
    """
    API 2 to return stored tweets and their metadata based on applied filters/search.
        a. API should be paginated
        b. It must support text search in tweet text/user name
        c. It must have sorting available by date time, tweet text, etc
        d. API should have filters like user/screen name, retweet count, favorite count, data
        range, language, user follower counts, user mentions, URLs, etc (the more, the
        merrier) in such a way that:
        i. Data range filter in case of date (e.g. tweet date, etc.)
        ii. Less than, greater than, equal to filter in case of integer column (e.g.
        retweet count)
        iii. Start with, ends with, contains, exact match in case of string (e.g. tweet
        text, user name, screen name, URLs, user mentions, etc.)

    EXAMPLE : http://127.0.0.1:8000/twitterSearch/


    :param request: ListAPIView
    :rtype: Response
    """
    # @ for exact search , DRF defaults icontains, ^ istartswith
    # search_fields = ['text', '^user', 'lang', '@retweet_count', '@favorite_count']
    search_fields = ['id', 'text', '$user', 'lang', 'retweet_count', 'favorite_count']
    filter_backends = (filters.SearchFilter,)
    queryset = TwitterData.objects.all()
    serializer_class = TwitterSearchSerializer
    pagination_class = TwitterSearchListPagination


def twitter_data_export(request):
    import pandas as pd
    df = pd.DataFrame({'id': [str(data.id) for data in TwitterData.objects.all()],
                       'text': [data.text for data in TwitterData.objects.all()],
                       'user': [data.user for data in TwitterData.objects.all()],
                       'lang': [data.lang for data in TwitterData.objects.all()],
                       'url': [str(data.url) for data in TwitterData.objects.all()]
                       }
                      )
    df.to_csv('./twitter.csv', encoding='UTF-8', index=False)
    result = {'msg': 'twitter.csv file created successfully'}
    return HttpResponse(json.dumps(result), content_type=application_type, status=status.HTTP_200_OK)
