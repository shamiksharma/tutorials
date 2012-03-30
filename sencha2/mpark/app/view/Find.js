/**
 * This screen is displayed once a user has logged in to Facebook and authorized our app.
 */
Ext.define('MP.view.Find', {
    extend: 'Ext.Panel',
    alias: 'widget.findview',
    xtype: 'findview',
    layout: 'vbox',


    config: {
        layout: 'card',

        items: [
            {
                title: 'Contact',
                iconCls: 'user',
                xtype: 'formpanel',
                id:'myFindPanel',
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
                                name:'location',
                                label: 'Location',
                                id:'locationField'
                            }
                        ]
                    },
                    {
                        xtype: 'button',
                        text: 'Find Parking',
                        id: 'findButton',
                        handler: function() {
                            console.log('firing event')
                            // this.getApplication().fireEvent('findEvent', "hello");
                        }
                    }
                ]
            }
        ]
    },

    initialize: function() {
        console.log('initialize find view');
    }
});