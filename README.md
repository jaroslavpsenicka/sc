## Detekce melanomu

Služba bere obrázek a vrací pravděpodobnost výskytu zhoubného (malign) nádoru.
Založeno na https://github.com/sotoblanco/skin-cancer-detection.

## URL
Služba běží na http://sc-test.eba-arpy6jtf.eu-west-1.elasticbeanstalk.com

## Příklad použití 
Zde je detekován zhoubný nádor.

```
$ curl -X POST -F "image=@melanome.jpg" http://sc-test.eba-arpy6jtf.eu-west-1.elasticbeanstalk.com/
{
  "benign": -0.24300161004066467,
  "malign": 2.030285358428955
}
```
