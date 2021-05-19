# API doc

##Create short url:
### POST http://0.0.0.0:8000/api/short/
{
    "url":"your link"
}
## Create short url:
### POST http://0.0.0.0:8000/api/delete/
{
  "initial":"your original link"
}
### OR
{
  "final":"short link without 'http://' "
}
