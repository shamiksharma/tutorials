Ext.define('MP.model.Parking', {
    extend: 'Ext.data.Model',

    config: {
        fields: [
            { name: 'location',  type: 'string' },
            { name: 'distance',  type: 'number' },
            { name: 'operator',  type: 'string' },
            { name: 'name',      type: 'string' }
        ]
    }
});