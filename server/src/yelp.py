import os
import rauth
from data import Data


class YelpApiWrapper(object):
    def __init__(self, consumer_key, consumer_secret, token, token_secret,
                 radius_filter=500, limit=20):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token = token
        self.token_secret = token_secret

        self.radius_filter = radius_filter
        self.limit = limit

    def get_search_parameters(self, latitude, longitude):
        params = dict()
        params["term"] = "restaurant"
        params["ll"] = "{},{}".format(str(latitude), str(longitude))
        params["radius_filter"] = str(self.radius_filter)
        params["limit"] = str(self.limit)

        return params

    def request_yelp_search(self, request_parameters):
        session = rauth.OAuth1Session(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.token,
            access_token_secret=self.token_secret)

        request = session.get(
            'http://api.yelp.com/v2/search',
            params=request_parameters)

        print request.url

        data = request.json()
        session.close()

        return data

    def yelp_geo_search_and_elastic_search_put(self, latitude, longitude):
        param = self.get_search_parameters(latitude, longitude)
        yelp_businesses = self.request_yelp_search(param)['businesses']

        for business in yelp_businesses:
            if not business.has_key('snippet_image_url'):
                business['snippet_image_url'] = 'http://rearviewcamera.net/crv/images/noimage.gif'

            if not business.has_key('url'):
                business['url'] = 'URL NOT FOUND'

            data = Data(
                instance_id=1,
                name=business['name'],
                geo=[
                    float(business['location']['coordinate']['latitude']),
                    float(business['location']['coordinate']['longitude'])
                ],
                reference_url=business['url'],
                reference_picture=business['snippet_image_url'],
                probability=float(business['review_count']) / 10000.0,
                reason='float(n_comments) / 10000.0',
                genre='Yelp Restaurant'
            )

            data.put()


if __name__ == '__main__':
    yelp = YelpApiWrapper(
        os.getenv('YELP_CONSUMER_KEY'),
        os.getenv('YELP_CONSUMER_SECRET'),
        os.getenv('YELP_TOKEN'),
        os.getenv('YELP_TOKEN_SECRET'))

    yelp.yelp_geo_search_and_elastic_search_put(35.6585, 139.7013)
