/**
 * This screen is displayed once a user has logged in to Facebook and authorized our app.
 */
Ext.define('MP.view.List', {
    extend: 'Ext.Container',
    alias: 'widget.listview',
    xtype: 'listview',

    requires: [
        //'MP.view.List',
    ],

    config: {
        layout: 'card',

        store: 'Parking',

        items: [
            {
                    title: 'Home',
                    iconCls: 'home',
                    cls: 'home',

                    html: [
                        //'<img src="http://staging.sencha.com/img/sencha.png" />',
                        '<h1>Welcome to List view</h1>'
                    ].join("")
            },
        ]
    }

});