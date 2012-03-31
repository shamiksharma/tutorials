
- System model is
    App = { api_token: '231aqr1r213.." }
    Event = {name:'sss', properties: {...} }
   
- The whole system is oriented towards 
   charting #-events vs time
   for a given event-name
   filtered by property values/ranges

- It is NOT good for analysing property values and correlating
  one property with another. (data-mining) 

- For example, say you have user-signup-events, with user-demo
  data in property-values (age, sex, location). You can filter
  #-signups by age-group, location etc. but you cant analysze 
  age vs location, or sex vs. age etc.

- Has nice cohort analysis.

  You can send a one-time event (e.g. user signup) and then
  create a chart using a rule.

  Show we people who did [one-time-event-x]
  and are  [properties]    # e.g. in location CA
  then came back and did  [event-y]
  and are  [properties]    # e.g. browser, country, os  
  in date range [start-date] to [end-date]

- It is also focussed on real-time data collection
  (i.e. just send them the event, they'll add the timestamp).
  It is much more cumbersome to "import" events (e.g. a
  script that harvests events from logs). They do have an
  /import API, but each event has to be imported as well as
  sent via the real-time /track api. 
