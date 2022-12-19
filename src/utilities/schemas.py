GET_BOOKING_SCHEMA = {'firstname': {'type': 'string'},
                      'lastname': {'type': 'string'},
                      'totalprice': {'type': 'integer'},
                      'depositpaid': {'type': 'boolean'},
                      'bookingdates': {'type': 'dict',
                                       'schema':
                                           {'checkin': {'type': 'string'},
                                            'checkout': {'type': 'string'}}},
                      'additionalneeds': {'type': 'string'}}
