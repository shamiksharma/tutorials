
function createMarker(map, position, atitle, iconImg, shadowImg) {
     var image, shadow, marker;

    if (iconImg) {
        image = new google.maps.MarkerImage(
                    'resources/images/point.png',
                    new google.maps.Size(32, 31),
                    new google.maps.Point(0, 0),
                    new google.maps.Point(16, 31)
                );
        shadow = new google.maps.MarkerImage(
                    'resources/images/shadow.png',
                    new google.maps.Size(64, 52),
                    new google.maps.Point(0, 0),
                    new google.maps.Point(-5, 42)
                );
        marker = new google.maps.Marker({
                    position: position,
                    title: atitle,
                    shadow: shadow,
                    icon: image,
                    map:map
                });
    }
    else {
        marker = new google.maps.Marker({
                position: position,
                title : atitle,
                map: map
            });
    }

    var infowindow = new google.maps.InfoWindow({content: atitle});

    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map, marker);
    });

    return marker;
}

var georesults = {};  //hack - made it global to get access in callback
var me;

function geocode(address, func) {
    console.log ("in codeaddress");
    var geocoder = new google.maps.Geocoder();
    console.log ("in codeaddress..2" + geocoder);
    geocoder.geocode( { 'address': address}, func);
}


Ext.define('MP.view.Map', {

    extend: 'Ext.Container',
    //alias: 'widget.mapview',
    xtype: 'mapview',

    requires: [
        //'MP.view.List',
        'Ext.Map',
        'Ext.Button',
        'Ext.SegmentedButton',
        'Ext.Panel',
        'Ext.Toolbar',
        'Ext.plugin.google.Traffic',
        'Ext.plugin.google.Tracker'
    ],

// items: [mapdemo] added dynamically by initialize()
    config: {
        fullscreen: true,
        layout: 'fit',
        items : [{}]
    },

    initialize: function() {
        me = this;
        geocode('San Deigo', this.showmap);
    },

    showmap: function(results, status) {

        console.log ('in callback' + status + results);

        if (status == google.maps.GeocoderStatus.OK) {
            console.log (results);
            georesults['lat'] = results[0].geometry.location.lat();
            georesults['lng'] = results[0].geometry.location.lng();
            console.log('lat ' + georesults['lat']);
            console.log('lng ' + georesults['lng']);
        }
        else {
            console.log("Geocode was not successful : " + status);
        }


        console.log('initializing map view....');

        console.log ('georesults are here');
        console.log (georesults);

        var centerLat = georesults['lat'];
        var centerLong = georesults['lng'];

        console.log('center lat is:' + centerLat);
        console.log('center Long is:' + centerLong);

        /*
        var centerLat = 37.44885 ;
        var centerLong = -122.158592 ;
        */

        var searchPos = new google.maps.LatLng(centerLat, centerLong);
      
        var mapdemo = Ext.create('Ext.Map', {

            mapOptions : {
                center : searchPos,  //nearby San Fran
                zoom : 14,
                mapTypeId : google.maps.MapTypeId.ROADMAP,
                navigationControl: true,
                navigationControlOptions: {
                    style: google.maps.NavigationControlStyle.DEFAULT
                },
                useCurrentLocation: true
            },
            /*
            plugins : [

                new Ext.plugin.google.Tracker({
                    trackSuspended: false,   //suspend tracking initially
                    allowHighAccuracy: false,
                    marker: createMarker(null,
                                searchPos,
                                'Current Location',
                                'resources/images/point.png',
                                'resources/images/shadow.png'
                            )
                }),
                new Ext.plugin.google.Traffic()
         
            ],
   */
            listeners: {
                maprender: function(comp, map) {
                    var marker = createMarker(map, searchPos, 'SenchaHQ');
                    setTimeout(function() {
                        map.panTo(searchPos);
                    }, 1000);
                }
            }
        });
        


        var gtracker   = new Ext.plugin.google.Tracker({
                            trackSuspended: false,   //suspend tracking initially
                            allowHighAccuracy: false,
                            marker: createMarker(
                                        null,
                                        searchPos,
                                        'Current Location',
                                        'resources/images/point.png',
                                        'resources/images/shadow.png'
                                    )
                        });

        var gtraffic  = new Ext.plugin.google.Traffic();

        console.log('initializing map view..2');

        //mapdemo.updatePlugins([gtracker, gtraffic], mapdemo.getPlugins());

        mapdemo.setPlugins([gtracker, gtraffic]);
        console.log(mapdemo);
        me.add(mapdemo);

    } //initialize

});

  

/*  A simpler setup - but less control to add content dynamically. */
/*
    config: {
        layout: 'card',
        store: 'Parking',
        items: [
            {
                xtype: 'map',
                layout: 'fit',
                id: 'cadwmap',
                fullscreen: true,
                mapOptions: {
                    zoom: 12,
                    //mapTypeId : google.maps.MapTypeId.ROADMAP,
                    //navigationControl: true,
                    //navigationControlOptions: {
                    //    style: google.maps.NavigationControlStyle.DEFAULT
                    //}
                },
                
                listeners: {
                    maprender: function(component, map) {
                        map.setCenter(
                            new google.maps.LatLng(37.44885, -122.158592)
                        );
                    }
                }
            }
        ]
    },

    initialize: function() {
        console.log('initialize map view');
        this.callParent();
    }
});
*/

