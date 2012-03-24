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

    //icon: 'resources/images/icon.png',
    //phoneStartupScreen:  'resources/images/phone_startup.png',

    models: ['Parking'],
    views:  ['Main', 'Map','List','Find'],
    controllers: ['Parking'],
    stores: ['Parking'],

    launch: function() {
        Ext.create('MP.view.Main');
    }
});
