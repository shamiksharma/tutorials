
Ext.define('MP.view.Main', {
    extend: 'Ext.Panel',

    requires: [
        'MP.view.Find',
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
                title: 'My Parking',
          
                items: [
                    {
                        xtype: 'button',
                        text: 'Back',
                        ui: 'back',
                        id: 'backButton',
                        hidden:'true'
                    }
                ]
           
            },
            // Second docked  toolbar
     
            {
                xtype:'tabpanel',    // Not tabbar, that is sencha internal
                id : 'mypanel',
                tabBarPosition:'bottom',
                layout: {pack:'left'},   // doesnt work
                items: [
                    { title: 'Find', iconCls: 'search',    xtype: 'findview', id:'findpanel'},
                    { title: 'List', iconCls: 'info',      xtype: 'listview', id:'listpanel'},
                    { title: 'Map',  iconCls: 'bookmarks', xtype: 'mapview' , id:'mappanel'}
                ]
            }
        ]
    }
});

