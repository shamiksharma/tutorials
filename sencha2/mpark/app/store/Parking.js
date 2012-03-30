Ext.define('MP.store.Parking', {
    extend: 'Ext.data.Store',
    
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

        /*
        Taken from:
        https://github.com/edspencer/APOD/blob/master/app/store/Pictures.js
        */

        /*
        proxy: {
            type: 'jsonp',
            url: 'https://ajax.googleapis.com/ajax/services/feed/load?v=1.0&q=http://www.acme.com/jef/apod/rss.xml&num=20',
            
            reader: {
                type: 'json',
                rootProperty: 'responseData.feed.entries'
            }
        }
        */

    }
});