
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


    config: {
        fullscreen: true,
        layout: 'fit',
        items : [{}]    // items: [mapdemo] added dynamically by initialize()
        
    },
    
    initialize: function() {
        console.log('initializing map view');
 
        // The following is accomplished with the Google Map API
        var position = new google.maps.LatLng(37.44885, -122.158592),  //Sencha HQ

            infowindow = new google.maps.InfoWindow({content: 'Sencha HQ'}),

            //Tracking Marker Image
            image = new google.maps.MarkerImage(
                'resources/images/point.png',
                new google.maps.Size(32, 31),
                new google.maps.Point(0, 0),
                new google.maps.Point(16, 31)
            ),

            shadow = new google.maps.MarkerImage(
                'resources/images/shadow.png',
                new google.maps.Size(64, 52),
                new google.maps.Point(0, 0),
                new google.maps.Point(-5, 42)
            );

        console.log('initializing map view..1');

        var mapdemo = Ext.create('Ext.Map', {
            mapOptions : {
                center : new google.maps.LatLng(37.44885, -122.158592),  //nearby San Fran
                zoom : 14,
                mapTypeId : google.maps.MapTypeId.ROADMAP,
                navigationControl: true,
                navigationControlOptions: {
                    style: google.maps.NavigationControlStyle.DEFAULT
                }
            },

            plugins : [
                new Ext.plugin.google.Tracker({
                    trackSuspended: true,   //suspend tracking initially
                    allowHighAccuracy: false,
                    marker: new google.maps.Marker({
                        position: position,
                        title: 'My Current Location',
                        shadow: shadow,
                        icon: image
                    })
                }),
                new Ext.plugin.google.Traffic()
            ],

            listeners: {
                maprender: function(comp, map) {

                    map.setCenter(
                        new google.maps.LatLng(37.44885, -122.158592)
                    );

                    var marker = new google.maps.Marker({
                        position: position,
                        title : 'Sencha HQ',
                        map: map
                    });

                    google.maps.event.addListener(marker, 'click', function() {
                        infowindow.open(map, marker);
                    });

                    setTimeout(function() {
                        map.panTo(position);
                    }, 1000);
                }
            }
        });

        console.log('initializing map view..2');

        this.add(mapdemo);
        //this.items.add(mapdemo);

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

