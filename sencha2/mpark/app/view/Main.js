/**
 * This screen is displayed once a user has logged in to Facebook and authorized our app.
 */
Ext.define('MP.view.Main', {
    extend: 'Ext.Panel',
    alias: 'widget.mainview',
    xtype: 'mainview',
    layout: 'vbox',


    config: {
        layout: 'card',

        items: [
            {
                title: 'Contact',
                iconCls: 'user',
                xtype: 'formpanel',
                url: 'contact.php',
                layout: 'vbox',

                items: [
                    {
                        xtype: 'fieldset',
                        //title: 'Contact Us',
                        instructions: '(Leave empty to use GPS)',
                        items: [
                            {
                                xtype: 'textfield',
                                label: 'Location'
                            }
                        ]
                    },
                    {
                        xtype: 'button',
                        text: 'Find Parking',
                        ui: 'confirm',
                        handler: function() {
                            this.up('formpanel').submit();
                        }
                    },
                    {
                        title: 'Home',
                        iconCls: 'home',
                        cls: 'home',

                        html: [
                            //'<img src="http://staging.sencha.com/img/sencha.png" />',
                            '<h1>Welcome to Main view</h1>'
                        ].join("")
                    }
                ]
            }
        ]
    },

    initialize: function() {
        console.log('initialize main view');
        this.callParent();
    }
    
});