Install
========

- Just checkout the git repos
  git@github.com:shamiksharma/tutorials.git

- Install sencha2 somewhere
  

Todo
=======
* Sample app
* Structuring with MVC architecture
* Getting views working
* Google Maps
* Using controllers and to tie things together
- Passing data from one page to another via store (e.g location)
- Using ajax to load data from apis
- Connecting with a real server
- load data from a local json file

Pages
=====
Main Page
- Loading screen

Find Page
- [ My Parking ]
  [ Location :    ]
  [ Submit ]
   
Parking Page - MapView
- [ Back   My Parking   ]
  [ Map with places  ]
    click on place shows popup with price and detail button
  [ List View  |  Map View ]

Parking Page - ListView
- [ Back   My Parking    ]
  [  List of places   > Detail Button ]
  [  List View | Map View ]

Place Page - Detail View
- [ Back   My Parking    ]
  [ Picture  Name,  Location, CurrentPrice ]
  [ Directions,   BookIt ]
  [ Rates ]

Directions Page - 
- [Back  My Parking ]
- Google map with directions

BookIt Page
- Stripe Form

Takeaways
=====
- Sencha2 has a layout structure much like Mxml/As3, but because
  it tries to fit into JS, it has a much more convoluted structure.
  Hard to tell the component hierarchy and properties/events of each component
- Lot of differences between Sencha Touch 1 and Sencha Touch 2 
  This makes documentation and looking up samples on the web hard
  (as a lot of samples dont apply to ST2)
- Performance is a huge issue. Takes ages to load my sample app on iPhone.

