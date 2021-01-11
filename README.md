# [This Land: Backend](https://this-land-team-5.herokuapp.com/admin/)

### ThisLand is a REST API built with Django, for use with the [ThisLand](https://this-land.netlify.app//) front-end app using React. 

The [This Land API](https://this-land-team-5.herokuapp.com/admin/) provides the backend & API of our this-land app. 'This Land' allows users to View, Create, Edit, and Delete Points of interest and the stories associated with them.

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
| GET | `/admin/` | Not so much for the API | But a very convenient admin panel |
| POST | `/auth/token/login/` | Returns Auth Token | Requires `username` and `password` |

| POST | `/pointsofinterest/` | Creates a new POI model object |  |
| POST | `/tellyourstory/` | Creates a new TYS model object |  |

| GET | `/pointsofinterest/` | Returns a list of all objects in the PointOfInterest model |  |
| GET | `/tellyourstory/` | Returns a list of all objects in the TellYourStory model |  |

| GET | `/pointsofinterest/<int:PointOfInterest_id>/` | Returns the detail view for `<POI_pk>` |  |
| GET | `/tellyourstory/<int:TellYourStory_id>/` | Returns the detail view for `<TYS_pk>` |  |

| GET | `/pointsofinterest/<int:PointOfInterest_id>/delete/` | Returns the detail view for `<POI_pk>` |  |
| GET | `/tellyourstory/<int:TellYourStory_id>/delete/>/` | Returns the detail view for `<TYS_pk>` |  |

| GET | `/pointsofinterest/<int:PointOfInterest_id>/update/` | Returns the detail view for `<POI_pk>` |  |
| GET | `/tellyourstory/<int:TellYourStory_id>/update/` | Returns the detail view for `<TYS_pk>` |  |

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
