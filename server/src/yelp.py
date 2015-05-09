import rauth


class YelpApiWrapper(object):
    def __init__(self, consumer_key, consumer_secret, token, token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token = token
        self.token_secret = token_secret

    @classmethod
    def get_search_parameters(cls, latitude, longitude, radius_filter=2000, limit=20):
        params = dict()
        params["term"] = "restaurant"
        params["ll"] = "{},{}".format(str(latitude), str(longitude))
        params["radius_filter"] = str(radius_filter)
        params["limit"] = str(limit)

        return params

    def yelp_search(self, request_paramters):
        session = rauth.OAuth1Session(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.token,
            access_token_secret=self.token_secret)

        request = session.get("http://api.yelp.com/v2/search", params=request_paramters)

        data = request.json()
        session.close()

        return data