## Detekce melanomu
Služba bere obrázek a vrací pravděpodobnost výskytu jednotlivých typů melanomu.
Založeno na https://github.com/sotoblanco/skin-cancer-detection.

| Kód | Popis |
| --- | --- |
| akiec | Actinic keratoses and intraepithelial carcinomae (Bowen's disease) |
| bcc | Basal cell carcinoma |
| bkl | Benign keratosis-like lesions |
| df | Dermatofibroma |
| mel | Melanoma |
| nv | Melanocytic nevi |
| vasc | Pyogenic granulomas and hemorrhage |

## URL
Služba běží na http://sc-test.eba-arpy6jtf.eu-west-1.elasticbeanstalk.com

## Příklad použití 
Zde je detekován Melanom (mel), max. hodnota pravděpodobnosti.

```
$ curl -X POST -F "image=@melanome.jpg" http://sc-test.eba-arpy6jtf.eu-west-1.elasticbeanstalk.com/
{
    "akiec":-8.656548500061035,
    "bcc":-7.905943393707275,
    "bkl":-1.5978127717971802,
    "df":-8.937097549438477,
    "mel":2.712484121322632,
    "nv":0.7940394878387451,
    "vasc":-0.0019751577638089657
}
```
