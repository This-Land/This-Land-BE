# [This Land: Backend](https://this-land-team-5.herokuapp.com/admin/)

### ThisLand is a REST API built with Django, for use with the [ThisLand](https://this-land.netlify.app//) front-end app using React. 

The [This Land API](https://this-land-team-5.herokuapp.com/admin/) provides the backend & API of our this-land app. Barkley allows users to View, Create, Edit, and Delete Points of interest and the stories associated with them.

This was the final project for [Momentum Learning](https://www.momentumlearn.com/), created by [Philip Johnson](https://github.com/trident6) and [Babacar Diouf](https://github.com/babacardiouf544).

---------------------------------------------------------------

## Models
| Model | Notes |
| ----- | ----- |
| [PointOfInterest](https://this-land-team-5.herokuapp.com/api/pointsofinterest/) |  |
| [TellYourStory](https://this-land-team-5.herokuapp.com/api/tellyourstory) |  |

---------------------------------------------------------------

## Endpoints: 
| HTTP Method | Endpoint | Result | Notes |
| ----------- | -------- | -------| ----- |
| POST | `/<basic model>/` | Creates a new model object |  |
| GET | `/<basic model>/` | Returns a list of all objects of that model |  |
| GET | `/<basic model>/<obj_pk>/` | Returns the detail view for `<obj_pk>` |  |
| POST | `/auth/token/login/` | Returns Auth Token | Requires `username` and `password` |
| GET | `/admin/` | Not so much for the API | But a very convenient admin panel |

<!-- 
    path("pointsofinterest/", api_views.POIListView.as_view()),
    path('pointsofinterest/<int:PointOfInterest_id>/', api_views.POIDetailView.as_view()),
    path('pointsofinterest/<int:PointOfInterest_id>/delete/', api_views.POIDetailView.as_view()),
    path('pointsofinterest/<int:PointOfInterest_id>/update/', api_views.POIDetailView.as_view()),
    path("tellyourstory/", api_views.TYSListView.as_view()),
    path('tellyourstory/<int:TellYourStory_id>/', api_views.TYSDetailView.as_view()),
    path('tellyourstory/<int:TellYourStory_id>/delete/', api_views.TYSDetailView.as_view()),
    path('tellyourstory/<int:TellYourStory_id>/update/', api_views.TYSDetailView.as_view()), -->


|     | Friending/Following, Dogs, & Search |  |  |
| -------- | -------- | -------- | -------- |
| POST | `/users/<user_pk>/follow/` | Adds self.request.user to `user_pk`'s follower list |  |
| POST | `/users/<user_pk>/unfollow/` | Removes `self.request.user` from `user_pk`'s follower list |  |
| POST | `/users/<user_pk>/request/` | Creates a `Request` object with `self.request.user` as proposing & `<user_pk>` as recieving |  |
| POST | `/users/<user_pk>/unfriend/` | Removes `<user_pk>` from `self.request.user`'s friend's list (it's symmetrical=True), deletes 'Request' object instance |  |
| GET | `/users/search/?q=<search term>` | Returns a list of all users with `search term` in their user/first/last/dog's name |  |
| GET | `/dogs/name_search/?=<search tearm>` | Returns a list of all dogs with names that match `search term` |  |
| GET | `/dogs/tag_search/?=<search tearm>` | Returns a list of all dogs with attributes that match `search term` |  |
| GET | `/dogs/theirs/?p=<user_pk>` | Returns a list of all of `<user_pk>`'s dogs | NO "/" at the end of the url |
| POST | `/requests/<req_pk>/accept/` | Sets `request.accepted = True`, adds `request.proposing` to `self.request.user`'s friends and vice versa |  |
| POST | `/requests/<req_pk>/deny/` | Deletes `Request` object |  |

|  | Convos & Messaging |  |  |
| -------- | -------- | -------- | -------- |
| POST |   `/conversations/<convo_pk>/message/` | Creates a `Message` object - sender=`self`, convo=`<convo_pk>`, `read_by.add(self)` | Requires `body`, can include `image`, will not accept anything else |
| POST | `/messages/<msg_pk>/read/` | Adds `self.request.user` to the message's `read` M2M field |  |



---------------------------------------------------------------

## Model Construction

### PointOfInterest
```
{
    "user": ForeignKey(to=User)
    "location_name": TextField
    "notes": TextField
    "street_address": CharField
    "city": CharField
    "state": CharField
    "zipcode": CharField
    "images": ImageField
    "category": CharField
    "date_created": DateField
}
```
   
### TellYourStory
```
{
    "user": ForeignKey(to=User)
    "poi": ForeignKey(to=PointOfInterest)
    "text": TextField
    "images": ImageField
    "date_created": DateField
}
```
