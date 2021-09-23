import tweepy
import asyncio

consumer_key = "your_key"
consumer_secret = "your_secret"
acess_token = "your_token"
acess_token_secret = "your_secret_token"

def capturar():
  #OAuthHandler é responsavel por autenticar o twitter 
  authentication = tweepy.OAuthHandler(consumer_key,consumer_secret)
  #atribuição dos valores de tokens de acesso
  authentication.set_access_token(acess_token,acess_token_secret)

  api = tweepy.API(authentication)

  #conecting to twitter
  twitter = tweepy.API(authentication)

  #streaming no twitter
  class MyStreamListener(tweepy.StreamListener,):
    def on_status(self, status):
      print(status.user.screen_name)
          # se o atributo "retweeted_status" existir, sinalize este tweet como um retweet.
      is_retweet = hasattr(status, "retweeted_status")
        
            # verifica se o texto foi truncado
      if hasattr(status,"extended_tweet"):
        text = status.extended_tweet["full_text"]
      else:
        text = status.text

              # verifica se este é um tweet de citação.
      is_quote = hasattr(status, "quoted_status")
      quoted_text = ""
      if is_quote:
                  # verifica se o texto do tweet citado foi truncado antes de gravá-lo
        if hasattr(status.quoted_status,"extended_tweet"):
          quoted_text = status.quoted_status.extended_tweet["full_text"]
        else:
          quoted_text = status.quoted_status.text

              # remove caracteres que podem causar problemas com codificação csv
      remove_comma = ["\n"]
      for c in remove_comma:
        n_Text = text.replace(c," ")
        n_Quoted_text = quoted_text.replace(c, " ")
          
      remove_line_break = [","]
      for c in remove_line_break:
        newText = n_Text.replace(c, " ")
        newQuoted_text = n_Quoted_text.replace(c, " ")

      print(newText)
      print(newQuoted_text)

      with open("/dados/dados_Streaming.csv", "a", encoding='utf-8') as f:
        f.write("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.id_str,is_retweet,is_quote,newText,newQuoted_text))

      
    def on_error(self, status_code):
      print("Encountered streaming error (", status_code, ")")
      sys.exit()
    
  #criando um fluxo de streaming
  myStreamListener = MyStreamListener()
  myStream = tweepy.Stream(api.auth, listener=myStreamListener,tweet_mode='extended')

  with open("/dados/dados_Streaming.csv", "a", encoding='utf-8') as f:
    f.write("date,user,is_retweet,is_quote,text,quoted_text\n")
    tags = ["hate speech"]

  results = myStream.filter(track=['bolsonaro'],languages=['pt'])

  #imprime apenas o nome do usuario e seu texto

capturar
