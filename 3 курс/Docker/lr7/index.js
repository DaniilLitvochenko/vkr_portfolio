const express = require('express');
const app = express();
const port = 8080;
const path = require('path');
const session = require('express-session');

const passport = require('passport');
const YandexStrategy = require('passport-yandex').Strategy;
const VKontakteStrategy = require('passport-vkontakte').Strategy;

app.use(session({ secret: "supersecret", resave: true, saveUninitialized: true }));

let Users = [{ 'login': 'admin', 'email': 'danay2000@inbox.ru' }
];

const findUserByLogin = (login) => {
    return Users.find((element) => {
        return element.login == login;
    })
}

const findUserByEmail = (email) => {
    return Users.find((element) => {
        return element.email.toLowerCase() == email.toLowerCase();
    })
}

app.use(passport.initialize());
app.use(passport.session());


passport.serializeUser((user, done) => {
    done(null, user);
});

passport.deserializeUser(function(obj, done) {
    done(null, obj);
});

passport.use(new YandexStrategy({
        clientID: '3693fc2ed1ac46a48cc8e34596846edd',
        clientSecret: 'c37c17994f7d46c1ac0bd87091368617',
        callbackURL: "http://localhost:8080/auth/yandex/callback"
    },
    (accessToken, refreshToken, profile, done) => {
        let user = findUserByEmail(profile.emails[0].value);
  
        if (user) return done(null, user);

        done(true, null);
    }
));

passport.use(
    new VKontakteStrategy({
            clientID: '7895315',
            clientSecret: 'HLdDrTAN96Mh6CpQTK0A',
            callbackURL: "http://localhost:8080/auth/vkontakte/callback",
        },
        function verify(accessToken, refreshToken, params, profile, done) {
            process.nextTick(function() {
                return done(null, profile);
            });
        }
    )
);

const isAuth = (req, res, next) => {
    if (req.isAuthenticated()) return next();

    res.redirect('/sorry');
}


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'main.html'));
});
app.get('/sorry', (req, res) => {
    res.sendFile(path.join(__dirname, 'sorry.html'));
});
app.get('/auth/yandex', passport.authenticate('yandex'));

app.get('/auth/yandex/callback', passport.authenticate('yandex', { failureRedirect: '/sorry', successRedirect: '/private' }));

app.get('/private', isAuth, (req, res) => {
    res.send(req.user);
});

app.get("/auth/vkontakte", passport.authenticate("vkontakte"));

app.get(
    "/auth/vkontakte/callback",
    passport.authenticate("vkontakte", {
        successRedirect: "/private",
        failureRedirect: "/sorry",
    })
);

app.listen(port, () => console.log(`App listening on port ${port}!`))