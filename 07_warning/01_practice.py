import warnings  

warnings.filterwarnings("ignore", "Your application has authenticated using end user credentials")

#UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK. We recommend that most server applications use service accounts instead. If your application continues to use end user credentials from Cloud SDK, you might receive a "quota exceeded" or "API not enabled" error. For more information about service accounts, see https://cloud.google.com/docs/authentication/
# warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)
