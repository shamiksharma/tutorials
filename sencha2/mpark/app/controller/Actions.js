Ext.define('MP.controller.Actions', {
    extend: 'Ext.app.Controller',
    requires: ['Ext.MessageBox'],

    config: {
        control: {
            '#signout': {
                tap: 'onUserTap'
            },
            '#logoutButton': {
                tap: 'logout'
            }
        }
    },

    init: function() {
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
