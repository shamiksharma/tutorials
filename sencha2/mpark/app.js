/**
Ext.Loader.setPath({
    'Ext': './sdk/src',
    'Ext.plugin': './sdk/lib/plugin'
});


Ext.application({
    name: 'MP',
    icon: 'resources/images/icon.png',
    phoneStartupScreen:  'resources/images/phone_startup.png',

    models: [
        'Parking'
    ],

    views: [
        'Main',
        'Map',
        'List',
    ],

    controllers: [
        'BuyParking',
    ],

    stores: [
        'Parking',
    ],

    viewport: {
        autoMaximize: true,
    },

    launch: function() {
            Ext.create('Ext.Component', {
                fullscreen: true,
                padding: 20,
                html: [
                    '<p>Please read the source of app.js to set up this example locally.</p><br/>',
                ].join('')
            })
    }
});

**/

//TOFIX: What does this do ?
Ext.Loader.setConfig({
    enabled:true
});

//<debug>
Ext.Loader.setPath({
    'Ext': './sdk/src',
    'Ext.plugin': 'lib/plugin'
});
//</debug>


Ext.application({
    name: 'MP',

    models: [
        'Parking'
    ],

    views: [
        'Main',
        'Map',
        'List',
        'Viewport'
    ],

    controllers: [
        'Actions'
    ],

    stores: [
        'Parking'
    ],

    launch: function() {
        Ext.create('MP.view.Viewport');
    }
});

/*
Ext.application({
    name: 'MP',



    icon: 'resources/images/icon.png',
    phoneStartupScreen:  'resources/images/phone_startup.png',

    models: [
       'Parking'
    ],

    views: [
       'Main',
       'Map',
       'List'
    ],

    controllers: [
       'Actions'
    ],

    stores: [
       'Parking'
    ],

    viewport: {
        autoMaximize: true
    },


    launch: function() {
        Ext.create("Ext.tab.Panel", {
            fullscreen: true,
            tabBarPosition: 'bottom',

            items:
            [
                {
                    docked: 'top',
                    xtype: 'toolbar',
                    title: 'Mango Parking',
                    items:
                    [
                        {
                            xtype: 'button',
                            text: 'Back',
                            ui: 'back',
                            id: 'mainBack'
                        }
                    ]
                },
                {
                    title: 'Contact',
                    iconCls: 'user',
                    xtype: 'formpanel',
                    url: 'contact.php',
                    layout: 'vbox',

                    items:
                    [
                        {
                            xtype: 'fieldset',
                            title: 'Location',
                            instructions: '(Leave empty to use GPS)',
                            items:
                            [
                                {
                                    xtype: 'textfield',
                                    label: 'Location',
                                    id   : 'locationField',
                                    placeHolder: 'City or zip'
                                }
                            ]
                        },
                        {
                            xtype: 'button',
                            text: 'Find Parking',
                            ui: 'confirm',
                            id: 'findparking',
                            handler: function()
                            {
                                this.up('formpanel').submit();
                            }
                        }
                    ]
                }
            ]
        });
    },


    initialize: function() {
        this.callParent();

        // Enable the Tap event on the profile picture in the toolbar, so we can show a logout button
        var meta = Ext.getCmp('findparking');
        if (meta) {
            meta.element.on('tap', function(e) { meta.fireEvent('tap', meta, e); });
        }
        this.view.map = new this.view.Map();
    }

});

*/