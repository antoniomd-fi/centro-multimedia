import webbrowser

def openWindow(app):
    browser = webbrowser.get("chromium-browser")
    if app == "netflix":
        browser.open("https://www.netflix.com/mx/login",new=2, autoraise=True)
    if app == "hbo":
        browser.open("https://play.hbomax.com/signIn",new=2, autoraise=True)
    if app == "disney":
        browser.open("https://www.disneyplus.com/login",new=2, autoraise=True)
    if app == "star":
        browser.open("https://www.starplus.com/login",new=2, autoraise=True)
    if app == "prime":
        browser.open("https://www.primevideo.com/",new=2, autoraise=True)
    if app == "cruchyroll":
        browser.open("https://www.crunchyroll.com/es/login?source=store&next=/",new=2, autoraise=True)
    if app == "vix":
        browser.open("https://vix.com/es/iniciar-sesion",new=2, autoraise=True)
    if app == "blim":
        browser.open("https://www.blim.com/cuenta/ingresar",new=2, autoraise=True)
    if app == "paramount":
        browser.open("https://www.paramountplus.com/mx/signin/?redirectUrl=%2Faccount%2Fsignin%2F",new=2, autoraise=True)
    if app == "spotify":
        browser.open("https://accounts.spotify.com/es/login/",new=2, autoraise=True)
    if app == "deezer":
        browser.open("https://www.deezer.com/mx/login",new=2, autoraise=True)
    if app == "youtube":
        browser.open("https://music.youtube.com/",new=2, autoraise=True)
    if app == "cloudflare":
        browser.open("https://dash.cloudflare.com/login",new=2, autoraise=True)