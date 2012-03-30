Ext.define('MP.controller.Parking', {
    extend: 'Ext.app.Controller',
    requires: ['Ext.MessageBox'],

    config: {
        refs: {
            logout: '#logoutButton',
            find: '#findButton',
            back: '#backButton',
            panel: '#mypanel',
            mappanel: '#mappanel'
        },
        control: {
            logout : {
                tap: 'doLogout'
            },
            find : {
                tap: 'doFind'
            }
        },
        routes: {

        }
    },

    init: function() {
        this.getApplication().on({findEvent:this.testEvent,scope:this});
        //this.callParent();
        //Ext.getStore('Parking').on('load', this.onParkingLoad);
    },

    onParkingLoad: function(store) {
         //var main = Ext.getCmp('main');
         //main.setActiveItem(List);
    },

    showForm: function() {
    },

    hideForm: function() {
    },

    addParking: function() {
    },

    testEvent: function(param) {
        alert('test event : ' + param);
    },

    testAction: function() {
        alert('from controller');
    },

    doFind: function() {
        this.getBack().show();

        var locationString;

        var formPanel = Ext.getCmp('myFindPanel');
        if (!formPanel) console.log("not found form panel");
        var dict = formPanel.getValues();
        if (!dict) console.log("not found dict of formPanel");
        
        locationString = dict['location'];

        console.log('showed back: ' + locationString  );


        /*
        var mappanel = this.getMappanel();
        console.log('got map panel');
        this.getPanel().setActiveItem(mappanel);
        console.log('set active item');
        */
    }

});


/**
init: function() {
        this.callParent();

        Ext.getStore('Runs').on('load', this.onRunsLoad);
    },

    onRunsLoad: function(store) {

        var main = Ext.getCmp('main'),
            runList = Ext.getCmp('runList'),
            noFriends = Ext.getCmp('noFriends');

        if (store.getCount()) {
            if (!runList) {
                runList = Ext.create('JWF.view.run.List', {
                    id: 'runList'
                });
            }
            main.setActiveItem(runList);
        } else {
            if (!noFriends) {
                noFriends = Ext.create('JWF.view.NoFriends', {
                    id: 'noFriends',
                    data: JWF.userData
                });
            }
            main.setActiveItem(noFriends);
        }
*/
