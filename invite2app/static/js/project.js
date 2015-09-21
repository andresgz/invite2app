/* Project specific Javascript goes here. */
 FB.init({
  appId:FACEBOOK_APP_ID,
  cookie:true,
  status:true,
  xfbml:true
 });

 function FBInvite(){
    FB.ui({
      method: 'send',
      link: APP_URL,
    });
 }