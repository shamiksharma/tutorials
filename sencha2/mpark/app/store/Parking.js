Ext.define('MP.store.Parking', {
    extend: 'Ext.data.TreeStore',
    
    config: {
        autoLoad: true,
        
        model: 'MP.model.Parking',
        
        proxy: {
            type: 'ajax',
            url: 'data/data.json',
            reader: {
                type: 'json',
                rootProperty: 'items'
            }
        }
    }
});