#!/usr/bin/env python
# coding: utf-8

# # Definisjon av den deriverte
# 
# ```{admonition} Læringsutbytte
# :class: utbytte, dropdown
# I dette temaet arbeider vi med kompetansemålet:
# 
#  * forstå begrepene vekstfart, grenseverdi, derivasjon og kontinuitet, og bruke disse for å løse praktiske problemer
#  * bruke ulike strategier for å utforske og bestemme grenseverdier til funksjoner, og utforske og argumentere for anvendelser av grenseverdier
#  * bestemme den deriverte i et punkt geometrisk, algebraisk og ved numeriske metoder, og gi eksempler på funksjoner som ikke er deriverbare i gitte punkter
# 
# Etter å ha arbeidet med temaet, skal du:
# 
#  * finne gjennomsnittlig og momentan vekstfart med og uten digitale hjelpemidler
#  * kunne forklare og bruke definisjonen av den deriverte
#  * forklare hva vi mener med deriverbarhet
#  * avgjøre om en funksjon er deriverbar i et punkt
#  * forklare sammenhengen mellom deriverbarhet og kontinuitet
# ```
# 
# I 1T så vi på størrelsene [gjennomsnittlig](https://kstige.github.io/Matematikk-1T/docs/vekstfart/gjennomsnittligvekstfart.html) og [momentan](https://kstige.github.io/Matematikk-1T/docs/vekstfart/momentanvekstfart.html) vekstfart. 
# 
# ```{admonition} Gjennomsnittlig og momentan vekstfart
# :class: def
# Den gjennomsnittlige vektfarten til en funksjon $f(x)$ på et intervall $[x_1, x_2]$ er gitt ved
# 
# $$
# \frac{\Delta f(x)}{\Delta x} = \frac{f(x_2)-f(x_1)}{x_2-x_1}
# $$
# 
# Dette er det samme som stigningstallet til den rette linja gjennom punktene $(x_1, f(x_1))$ og $(x_2, f(x_2))$.
# 
# Den momentane vekstfarten til en funksjon i et punkt er lik stigningstallet til tangenten i punktet.
# ```
# 
# I appen under ser vi at når vi lar området vi tar den gjennomsnittlige vekstfarten overv bli mindre og mindre, så vil den gjennomsnittlige vekstfarten nærme seg den momentane vekstfarten. Dette likner på en grenseverdi og vi skal bruke det når vi i neste avsnitt gir en formell definisjon av dette begrepet.

# In[4]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script> \n   var views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 0,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\n   var parameters = {\n  "width":1550, "height":658, \n  "bordercolor": "#be8322", \n  "showResetIcon":true,\n  "enableLabelDrags":false,\n  "enableRightClick":false,\n  "errorDialogsActive":false,\n  "useBrowserForJS":false,\n  "showZoomButtons":true,\n  "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n  "showFullscreenButton":true,  \n  "disableAutoScale":false,\n  "allowUpscale":false,\n  "clickToLoad":false,\n  "appName":"classic",\n  "buttonRounding":0.7,\n  "buttonShadows":false,\n  "language":"nb",\n  "ggbBase64":"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"\n  };\n   var applet = new GGBApplet(parameters, \'5.0\', views);\n   window.addEventListener("load", function() { \n       applet.inject(\'ggb-element\');\n   });\n</script>\n\n<div id="ggb-element"></div> \n')


# 
# ## Definisjonen av den deriverte
# 
# Vi starter først med å gjengi definisjonen vi brukte i 1T før vi gir den presise og formelle definisjonen.
# 
# ```{admonition} Den deriverte
# :class: def
# 
# $f'(x)$ (leses "f derivert av x") er en funksjon som har funksjonsverdi lik stigningstallet til tangenten til $f(x)$ i punktet $(x, f(x))$.
# 
# Den deriverte i et punkt har samme verdi som den momentane vekstfarten i punktet.
# ```
# 
# ```{admonition} Definisjonen av den deriverte
# :class: def
# 
# Gitt funksjonen $f(x)$. Den deriverte av funksjonen $f(x)$ er definert ved
# 
# $$f'(x)=\lim_{\Delta x\to 0}\frac{\Delta f(x)}{\Delta x}=\frac{f(x+\Delta x)-f(x)}{\Delta x}$$
# 
# gitt at grenseverdien eksisterer.
# ```
# 
# Den formelle definisjonen kan virke litt kryptisk, men den sier det samme som 1T-definisjonen. For å gjøre det klarere, så skal vi prøve å forklare den ved ord. $\Delta$ er et symbol vi bruker for en endring, så når vi skriver $\Delta x$ mener vi en endring i $x$. Definisjonen sier altså at den deriverte er gitt ved endringen i funksjonsverd (endring langs y-aksen) dividert med endringen i $x$. Videre lar vi endringen i $x$ bli veldig, veldig liten.
# 
# Den gjennomsnittlige vekstfarten er endring i funksjonsverdi dividert med endring i $x$-verdi. Den deriverte er akkurat det samme bare at vi lar endringen i $x$ gå mot null. Da finner vi stigningstallet til tangenten.
# 
# Den formelle definisjonen sier altså matematisk den den *uformelle* sa med ord. Så en fordel med den formelle definisjonen er at den gir oss en kompakt matematisk skrivemåte. I tillegg vil vi kunne bruke den til å regne ut den deriverte funksjonen og etterhvert til å bevise generelle derivasjonsregler.
# 
# 
# ```{admonition} Eksempel: Derivert av $x^2$
# :class: def
# 
# Vi skal bruke definisjonen av den deriverte til å utlede en derivasjonsregel for $f(x)=x^2$.
# 
# $\begin{align}
# f'(x)&=\displaystyle\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x} \\
# &=\lim_{\Delta x\to 0}\frac{(x+\Delta x)^2-x^2}{\Delta x} \\
# &=\lim_{\Delta x\to 0}\frac{x^2+2x\Delta x + (\Delta x)^2-x^2}{\Delta x} \\
# &=\lim_{\Delta x\to 0}\frac{\Delta x (2x+\Delta x)}{\Delta x} \\
# &=\lim_{\Delta x\to 0} (2x+\Delta x) \\
# &= 2x
# \end{align}$
# 
# Vi ser altså at når $f(x)=x^2$, så vil $f'(x)=2x$.
# 
# Så om vi trenger den momentane vekstfarten til $f(x)$ for $x=4$, så vil den være $f'(4)=2\cdot 4=8$.
# ```
# 
# ```{admonition} Eksempel: Derivert av lineær funksjon
# :class: def
# 
# Vi skal bruke definisjonen av den deriverte til å utlede en derivasjonsregel for $f(x)=a\cdot x + b$, der $a,b\in\mathbf{R}$.
# 
# $\begin{align}
# f'(x)&=\displaystyle\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x} \\
# &=\lim_{\Delta x\to 0}\frac{a(x+\Delta x)+b-(ax+b)}{\Delta x} \\
# &=\lim_{\Delta x\to 0}\frac{ax+a\Delta x + b -ax-b}{\Delta x} \\
# &=\lim_{\Delta x\to 0}\frac{a\Delta x}{\Delta x} \\
# &=\lim_{\Delta x\to 0} a \\
# &= a
# \end{align}$
# 
# Vi ser altså at når $f(x)=ax+b$, så vil $f'(x)=a$.
# 
# Den deriverte til en lineær funksjon er altså stigningstallet til funksjonen. Det gir mening siden vi har sagt at den deriverte er lik stigningstallet til tangenten i hvert punkt, og tangenten til en lineær funksjon er funksjonen selv.
# ```

# ## Deriverbarhet og kontinuitet
# På neste side skal vi lære oss alt vi trenger av derivasjonsregler, men først vil vi ta for oss det som kanskje er den mest teoretiske delen av hele R1 faget. Det handler om sammenhengen mellom deriverbarhet og kontinuitet og forklarer på et dypere plan hvorfor mye av det vi gjør videre i faget vil fungere. Om det er vanskelig å forstå, så prøv og fokuser på bildene av grafene og ikke så mye på de matematiske uttrykkene. Det her er viktig for matematikken, men vi kan gjøre det aller meste videre uten å forstå det her.
# 
# Vi starter med å se på funksjonen i grafen under
# 
# ```{figure} ./bilder/deriverbarhet.png
# ---
# scale: 20%
# ---
# ```
# 
# Funksjonen har bruddpunkt i $x=-2$ og i $x=0$. I bruddpunktet i $x=-2$ ser vi at funksjonen er kontinuerlig, mens i $x=0$ er den ikke det. Det her ser vi tydelig fra grafen, men prøv gjerne å vise det også med grenseverdier. For analyse av funksjoner, så er det viktig å kunne si noe om kontinuitet. Like viktig er det å kunne si noe om funksjonen er deriverbar.
# 
# Vi vet at den deriverte er lik stigningstallet til tangenten i et punkt. En naturlig definisjon av deriverbarhet blir da:
# 
# ```{admonition} Deriverbarhet
# :class: def
# En funksjon $f(x)$ er deriverbar for $x=a$ dersom vi kan tegne inn en tangent i punktet $(a, f(a))$ på grafen til $f$.
# 
# Om vi ikke kan tegne inn en tangent, så er funksjonen ikke deriverbar i punktet.
# ```
# 
# Fra grafen over ser vi at vi vil få problemer med å tegne inn tangenter i de to bruddpunktene. Funksjonen er altså ikke deriverbar i punktene.
# 
#  * I $x=-2$ går tangenten fra å ha stigningstall $-1$ til å ha stigningstall $1$. Et slikt punkt der grafen er kontinuerlig, men ikke deriverbar kaller vi et **knekkpunkt**.
#  * I $x=0$ er ikke funksjonen kontinuerlig. En tangent som kommer fra venstre og en som kommer fra høyre vil ikke være lik hverandre i punktet og funksjonen er ikke deriverbar.
# 
# Stopp opp og gå gjennom de forrige avsnittene en gang til. Det forklarer med ord og grafer det vi nå skal formulere matematisk.
# 
# ```{admonition} Formell definisjon på deriverbarhet
# :class:
# 
# En funksjon $f$ er deriverbar for $x=a$ dersom grenseverdien
# 
# $$\lim_{\Delta x\to 0}\frac{f(a+\Delta x)-f(a)}{\Delta x}$$ 
# 
# eksisterer. Dette er egentlig bare definisjonen av den deriverte for $x=a$.
# 
# For at grenseverdien over skal eksistere må de to ensidige grenseverdiene ($\Delta x \to 0^-$ og $\Delta x \to 0^+$) eksistere og være like.
# 
# I noen tilfeller vil det være enklere å omformulere definisjonen over ved å sette inn at $\Delta x = x-a$. Vi får da formen under, men vi skal prøve å holde oss til den definisjonen som minner mest om definisjonen på den deriverte.
# 
# $$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$ 
# ```
# 
# ```{admonition} Eksempel: Ikke-deriverbar funksjon
# :class: eksempel
# 
# Vi ser på funksjonen $f(x)=\begin{cases} 
#       |x+2| \text{når } \quad x\leq 0 \\
#       4-x^2 \text{når } \quad x>0
#    \end{cases}$ 
# som vi innledet temaet med. Den har vi allerede sett at ikke er deriverbar for $x=-2$ go $x=0$. Det skal vi nå vise algebraisk.
# 
# **$x=-2$**
# Vi ser på den venstresidige og den høyresidige grensen av den deriverte i punktet.
# 
# $\displaystyle\lim_{\Delta x\to 0^-}\frac{f(2+\Delta x)-f(2)}{\Delta x} =\lim_{\Delta x\to 0^-}\frac{-(-2+\Delta x +2)-0}{\Delta x}=\lim_{\Delta x\to 0^-}\frac{-\Delta x}{\Delta x}=-1$
# 
# $\displaystyle\lim_{\Delta x\to 0^+}\frac{f(2+\Delta x)-f(2)}{\Delta x} =\lim_{\Delta x\to 0^+}\frac{(-2+\Delta x +2)-0}{\Delta x}=\lim_{\Delta x\to 0^+}\frac{\Delta x}{\Delta x}=1$
# 
# Den venstresidige og høyresidige grenseverdien er ulik. Derfor er funksjonen ikke deriverbar for $x=-2$.\
# *Over har vi brukt at $|x+2|=-(x+2)$ for $x<-2$ og $|x+2|=x+2$ for $x>-2$.*
# 
# **$x=0$**
# Vi gjør tilsvarende
# 
# $\displaystyle\lim_{\Delta x\to 0^-}\frac{f(0+\Delta x)-f(0)}{\Delta x} =\lim_{\Delta x\to 0^-}\frac{(0+\Delta x +2)-2}{\Delta x}=\lim_{\Delta x\to 0^-}\frac{\Delta x}{\Delta x}=1$
# 
# $\displaystyle\lim_{\Delta x\to 0^+}\frac{f(0+\Delta x)-f(0)}{\Delta x} =\lim_{\Delta x\to 0^+}\frac{(4-(0+\Delta x)^2)-4}{\Delta x}=\lim_{\Delta x\to 0^+}\frac{(\Delta x)^2}{\Delta x}=0$
# 
# Den venstresidige og høyresidige grenseverdien er ulik. Derfor er funksjonen ikke deriverbar for $x=0$.
# ```
# 
# Til slutt skal vi vise en viktig sammenheng mellom deriverbarhet og kontinuitet.
# 
# ```{admonition} Sammenheng mellom deriverbarhet og kontinuitet
# :class: def
# 
# $f(x)$ er deriverbar i $x=a \quad \Rightarrow \quad f(x)$ er kontinuerlig i $x=a$.
# 
# $f(x)$ er ikke kontinuerlig i $x=a \quad \Rightarrow \quad f(x)$ er ikke deriverbar i $x=a$.
# 
# Merk at begge sammenhengene er implikasjoner og ikke ekvivalenser. Vi kan derfor **ikke** si
# 
#  * $f(x)$ er deriverbar dersom den er kontinuerlig
#  * $f(x)$ er ikke kontinuerlig dersom der ikke er deriverbar
# 
# Punktet $x=-2$ er et eksempel på dette.
# ```
# 
# ```{admonition} Bevis for sammenhengen
# :class: def, dropdown
# 
# Vi har sett at en funksjon er deriverbar i $x=a$ dersom grenseverdien under eksisterer.
# 
# $$\lim_{\Delta x\to 0}\frac{f(a+\Delta x)-f(a)}{\Delta x}$$
# 
# I den grensa, så ser vi at nevneren går mot null. Om grenseverdien skal eksistere, så må samtidig telleren gå mot null (hvis ikke går grensa mot uendelig).
# 
# $\displaystyle\lim_{\Delta x\to 0}(f(a+\Delta x)-f(a))=\lim_{\Delta x\to 0}f(a+\Delta x)-\lim_{\Delta x\to 0}f(a)=\lim_{\Delta x\to 0}f(a+\Delta x) - f(a)=0$
# 
# Da må $\displaystyle\lim_{\Delta x\to 0} f(a+\Delta x)=f(a)$ som viser at funksjonen er kontinuerlig.
# 
# Vi har da vist
# 
# $f(x)$ er deriverbar i $x=a \quad \Rightarrow \quad f(x)$ er kontinuerlig i $x=a$
# ```
# 
# 
