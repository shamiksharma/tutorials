
Ext.define('MP.view.Viewport', {
    extend: 'Ext.Panel',

    requires: [
        'MP.view.Main',
        'MP.view.List',
        'MP.view.Map'
    ],

    config : {
        fullscreen: true,
        layout:'card',

        items : [
            {
                xtype: 'toolbar',
                docked: 'top',
                title: 'Mango Parking',
                items: [
                    {
                        xtype: 'button',
                        text: 'Back',
                        ui: 'back',
                        id: 'addRunBackBtn'
                    }

                ]
            },
            // Second docked  toolbar
            {
                xtype:'tabpanel',    // Not tabbar, that is sencha internal
                tabBarPosition:'bottom',
                layout: {pack:'left'},   // doesnt work
                items: [
                    { title: 'Find', iconCls: 'search',    xtype: 'mainview'},
                    { title: 'List', iconCls: 'info',      xtype: 'listview'},
                    { title: 'Map',  iconCls: 'bookmarks', xtype: 'mapview' }
                ]
            } 
        ]
    } 
});

