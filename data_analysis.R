data <- read.csv('~/gml_projekti/postcode_data.csv')
data$KuntoNum = data$Kunto
attach(data)
as.numeric(Kunto)
fit1 <- lm(Vh ~ (m2 + Rv + vaestontiheys+Kunto))
fit2 <- lm(Vh ~ (m2 + Rv + vaestontiheys+Kunto)^2)
fit3 <- lm(Vh ~ (m2 + Rv + vaestontiheys+Kunto)^3)
anova(fit1, fit2)
summary(fit3)

fit3 <- lm(Vh ~ (m2 + Rv + vaestontiheys+Kunto + m2*Kunto))
summary(fit3)
summary(fit1)
Kunto
