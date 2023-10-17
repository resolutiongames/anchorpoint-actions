# anchorpoint-actions
Anchorpoint actions repository


#Instructions on adding a history tracker
1. Dive into the actions/clouddrive code and expose the json data when uploading to the cloud
2. Extract the file properties from this data
3. Anchorpoint is exposing the ctx.username to the API
4. Create an attribute where the last usernam who modified the file can be shown
5. Use python to generate a metafile with the files history
6. Auto-open that file on-demand or something similar
