info.player4.onLifeZero(function () {
    game.setDialogTextColor(1)
    game.setDialogFrame(img`
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        `)
    if (!(info.player1.hasLife()) && (!(info.player2.hasLife()) && !(info.player3.hasLife()))) {
        game.showLongText("Player 4 Wins!", DialogLayout.Bottom)
        game.over(true)
    } else {
        game.showLongText("Player 4 is out :-(", DialogLayout.Bottom)
        player4.destroy()
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    if (sprite2 == player1) {
        info.player1.changeLifeBy(-1)
        scene.cameraShake(4, 200)
    } else if (sprite2 == player2) {
        info.player2.changeLifeBy(-1)
        scene.cameraShake(4, 200)
    } else if (sprite2 == player3) {
        info.player3.changeLifeBy(-1)
        scene.cameraShake(4, 200)
    } else {
        info.player4.changeLifeBy(-1)
        scene.cameraShake(4, 200)
    }
    otherSprite2.destroy(effects.fire, 200)
})
info.player3.onLifeZero(function () {
    game.setDialogTextColor(1)
    game.setDialogFrame(img`
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        `)
    if (!(info.player1.hasLife()) && (!(info.player2.hasLife()) && !(info.player4.hasLife()))) {
        game.showLongText("Player 3 Wins!", DialogLayout.Bottom)
        game.over(true)
    } else {
        game.showLongText("Player 3 is out :-(", DialogLayout.Bottom)
        player3.destroy()
    }
})
controller.player3.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    if (info.player3.hasLife()) {
        dart3 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 5 a a 8 . . . . . . . . . . . 
            5 5 a 8 8 8 8 4 4 4 4 . . . . . 
            . 5 a a 8 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, player3, 200, 0)
    }
})
info.player1.onLifeZero(function () {
    game.setDialogTextColor(1)
    game.setDialogFrame(img`
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        `)
    if (!(info.player2.hasLife()) && (!(info.player3.hasLife()) && !(info.player4.hasLife()))) {
        game.showLongText("Player 1 Wins!", DialogLayout.Bottom)
        game.over(true)
    } else {
        game.showLongText("Player 1 is out :-(", DialogLayout.Bottom)
        player1.destroy()
    }
})
controller.player4.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    if (info.player4.hasLife()) {
        dart4 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 5 a a 5 . . . . . . . . . . . 
            5 5 a 5 5 5 5 4 4 4 4 . . . . . 
            . 5 a a 5 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, player4, 200, 0)
    }
})
info.player2.onLifeZero(function () {
    game.setDialogTextColor(1)
    game.setDialogFrame(img`
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f 
        `)
    if (!(info.player1.hasLife()) && (!(info.player3.hasLife()) && !(info.player4.hasLife()))) {
        game.showLongText("Player 2 Wins!", DialogLayout.Bottom)
        game.over(true)
    } else {
        game.showLongText("Player 2 is out :-(", DialogLayout.Bottom)
        player2.destroy()
    }
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    if (info.player2.hasLife()) {
        dart2 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 5 a a 7 . . . . . . . . . . . 
            5 5 a 7 7 7 7 4 4 4 4 . . . . . 
            . 5 a a 7 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, player2, 200, 0)
    }
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    if (info.player1.hasLife()) {
        dart1 = sprites.createProjectileFromSprite(assets.image`test`, player1, 200, 0)
    }
})
controller.player1.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    // No need for '== True'
    if (info.player1.hasLife()) {
        dart1 = sprites.createProjectileFromSprite(background, player1, 200, 0)
    }
    if (info.player2.hasLife()) {
        dart2 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 5 a a 7 . . . . . . . . . . . 
            5 5 a 7 7 7 7 4 4 4 4 . . . . . 
            . 5 a a 7 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, player2, 200, 0)
    }
    if (info.player3.hasLife()) {
        dart3 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 5 a a 8 . . . . . . . . . . . 
            5 5 a 8 8 8 8 4 4 4 4 . . . . . 
            . 5 a a 8 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, player3, 200, 0)
    }
    if (info.player4.hasLife()) {
        dart4 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 5 a a 5 . . . . . . . . . . . 
            5 5 a 5 5 5 5 4 4 4 4 . . . . . 
            . 5 a a 5 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, player4, 200, 0)
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    if (sprite == dart1) {
        info.player1.changeScoreBy(1)
    } else if (sprite == dart2) {
        info.player2.changeScoreBy(1)
    } else if (sprite == dart3) {
        info.player3.changeScoreBy(1)
    } else {
        info.player4.changeScoreBy(1)
    }
    sprite.destroy()
    otherSprite.destroy(effects.fire, 500)
})
let bogey: Sprite = null
let dart1: Sprite = null
let dart2: Sprite = null
let dart4: Sprite = null
let dart3: Sprite = null
let player4: Sprite = null
let player3: Sprite = null
let player2: Sprite = null
let player1: Sprite = null
let background: Image[] = []
let test = [img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . 2 2 3 3 3 3 2 . . . . 
    . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
    . 1 1 1 1 1 1 1 1 1 1 1 2 . . . 
    . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
    . . . . . 2 2 2 3 3 3 2 . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . 2 2 . . . . . . . . . . . . . 
    . 3 1 1 3 . . . . . . . . . . . 
    . 1 1 1 1 2 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    . 3 1 1 1 2 . . . . . . . . . . 
    . 3 1 1 3 . . . . . . . . . . . 
    . 2 2 . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,img`
    . . . . . . . . . . . . . . . . 
    . . . . . 2 2 4 4 4 . . . . . . 
    . . 2 . 2 d 5 5 d 5 4 4 . . . . 
    . 2 2 2 4 5 5 5 d 5 5 d 4 . . . 
    . 2 2 2 d 5 5 1 1 5 5 5 4 . . . 
    2 4 2 4 d d d 1 1 1 1 d 4 4 . . 
    2 4 2 d 5 1 1 5 5 1 1 5 5 4 . . 
    2 4 4 5 5 1 1 1 5 1 1 5 5 4 . . 
    2 4 4 5 5 1 1 1 5 5 d 5 5 4 . . 
    2 4 4 d 5 5 5 5 1 1 d d d 4 . . 
    2 4 2 d d 1 1 5 1 1 5 d 4 . . . 
    . 2 2 4 d 1 1 d 5 5 5 d 4 . . . 
    . 2 2 4 5 5 5 d 5 5 5 4 4 . . . 
    . . . . 4 5 5 d d 4 4 4 4 . . . 
    . . . . . 2 2 4 4 4 . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,img`
    . . . 2 2 4 4 4 . . b b b . . . 
    . 2 2 2 4 4 4 4 . b d d b . . . 
    . 2 4 4 4 5 5 4 b d d d d b 2 . 
    . 2 4 5 4 5 5 4 b d b b 1 b 2 2 
    2 4 4 4 d 5 5 . b d b b 1 1 4 2 
    2 4 4 5 5 d d . b d b b d d 4 2 
    2 4 5 5 5 d 5 5 2 2 2 b 1 d 4 4 
    2 5 5 5 5 d 5 5 4 4 4 b d 3 4 4 
    2 5 5 d 5 5 d 4 4 4 4 b 1 1 4 4 
    2 4 4 5 5 5 4 2 2 2 2 b 1 1 4 4 
    2 4 d 5 5 5 4 . b d b b 3 d 4 4 
    2 4 5 5 d d 4 . b d b b 1 d 4 2 
    . 2 5 5 d 5 5 4 b d b b 1 b 2 2 
    . . 2 4 4 5 5 4 b d d d d b 2 . 
    . . 2 2 2 4 4 4 . b d d b . . . 
    . . . . . 2 2 4 . . b b b . . . 
    `,img`
    . . . . b b . . . . . b c c c . 
    . . . b d d b . . . b d d c c . 
    . . . b d d b . . b d d d d c . 
    . . . . b b . . . b d c c d c . 
    . . . . . . . . . b c c b b c . 
    . . . . . b b . . d c b . . c . 
    b b . . . b b . . d b . . . . . 
    b b . . . . . . . d b . . . b c 
    . . . . . . . . . d b . . . d c 
    . . . . . . . . . d b . . b d c 
    . . b b b . . . . d c . . b d c 
    . . b d d b . . . b c b b d d c 
    . . b d d d b . . b c c b d b c 
    . . . b d d b . . b d d d d c . 
    . . . . b b b . . . b d d b c . 
    . . . . . . . . . . . b c c . . 
    `]
background = [img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . 2 2 3 3 3 3 2 . . . . 
    . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
    . 1 1 1 1 1 1 1 1 1 1 1 2 . . . 
    . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
    . . . . . 2 2 2 3 3 3 2 . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . 2 2 . . . . . . . . . . . . . 
    . 3 1 1 3 . . . . . . . . . . . 
    . 1 1 1 1 2 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    2 1 1 1 1 3 . . . . . . . . . . 
    . 3 1 1 1 2 . . . . . . . . . . 
    . 3 1 1 3 . . . . . . . . . . . 
    . 2 2 . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,img`
    . . . . . . . . . . . . . . . . 
    . . . . . 2 2 4 4 4 . . . . . . 
    . . 2 . 2 d 5 5 d 5 4 4 . . . . 
    . 2 2 2 4 5 5 5 d 5 5 d 4 . . . 
    . 2 2 2 d 5 5 1 1 5 5 5 4 . . . 
    2 4 2 4 d d d 1 1 1 1 d 4 4 . . 
    2 4 2 d 5 1 1 5 5 1 1 5 5 4 . . 
    2 4 4 5 5 1 1 1 5 1 1 5 5 4 . . 
    2 4 4 5 5 1 1 1 5 5 d 5 5 4 . . 
    2 4 4 d 5 5 5 5 1 1 d d d 4 . . 
    2 4 2 d d 1 1 5 1 1 5 d 4 . . . 
    . 2 2 4 d 1 1 d 5 5 5 d 4 . . . 
    . 2 2 4 5 5 5 d 5 5 5 4 4 . . . 
    . . . . 4 5 5 d d 4 4 4 4 . . . 
    . . . . . 2 2 4 4 4 . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,img`
    . . . 2 2 4 4 4 . . b b b . . . 
    . 2 2 2 4 4 4 4 . b d d b . . . 
    . 2 4 4 4 5 5 4 b d d d d b 2 . 
    . 2 4 5 4 5 5 4 b d b b 1 b 2 2 
    2 4 4 4 d 5 5 . b d b b 1 1 4 2 
    2 4 4 5 5 d d . b d b b d d 4 2 
    2 4 5 5 5 d 5 5 2 2 2 b 1 d 4 4 
    2 5 5 5 5 d 5 5 4 4 4 b d 3 4 4 
    2 5 5 d 5 5 d 4 4 4 4 b 1 1 4 4 
    2 4 4 5 5 5 4 2 2 2 2 b 1 1 4 4 
    2 4 d 5 5 5 4 . b d b b 3 d 4 4 
    2 4 5 5 d d 4 . b d b b 1 d 4 2 
    . 2 5 5 d 5 5 4 b d b b 1 b 2 2 
    . . 2 4 4 5 5 4 b d d d d b 2 . 
    . . 2 2 2 4 4 4 . b d d b . . . 
    . . . . . 2 2 4 . . b b b . . . 
    `,img`
    . . . . b b . . . . . b c c c . 
    . . . b d d b . . . b d d c c . 
    . . . b d d b . . b d d d d c . 
    . . . . b b . . . b d c c d c . 
    . . . . . . . . . b c c b b c . 
    . . . . . b b . . d c b . . c . 
    b b . . . b b . . d b . . . . . 
    b b . . . . . . . d b . . . b c 
    . . . . . . . . . d b . . . d c 
    . . . . . . . . . d b . . b d c 
    . . b b b . . . . d c . . b d c 
    . . b d d b . . . b c b b d d c 
    . . b d d d b . . b c c b d b c 
    . . . b d d b . . b d d d d c . 
    . . . . b b b . . . b d d b c . 
    . . . . . . . . . . . b c c . . 
    `]
game.splash("Ask your friends to join", "Then press A")
effects.starField.startScreenEffect()
player1 = sprites.create(img`
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ....82..........................
    ....111.....999999..............
    ....2222...99999999.............
    .444.8222222999999222...........
    422.22222222222222222222........
    .44.288822222222222222222.......
    ..44.88.....222222222222........
    ...........22222228.............
    ...........2222228..............
    ..........2222228...............
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    `, SpriteKind.Player)
player1.setPosition(20, 15)
player1.setFlag(SpriteFlag.StayInScreen, true)
controller.moveSprite(player1, 200, 200)
info.player1.setLife(3)
info.player1.setScore(0)
player2 = sprites.create(img`
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ....8a..........................
    ....111.....999999..............
    ....aaaa...99999999.............
    .aaa.c888888999999888...........
    a88.88888888888888888888........
    .aa.8ccc88888888888888888.......
    ..aa.cc.....888888888888........
    ...........88888885.............
    ...........8888885..............
    ..........8888885...............
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    `, SpriteKind.Player)
player2.setPosition(20, 45)
player2.setFlag(SpriteFlag.StayInScreen, true)
controller.player2.moveSprite(player2, 200, 200)
info.player2.setLife(3)
info.player2.setScore(0)
player3 = sprites.create(img`
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ....4a..........................
    ....111.....999999..............
    ....aaaa...99999999.............
    .aaa.7444444999999444...........
    a44.44444444444444444444........
    .aa.477444444444444444444.......
    ..aa.77.....444444444444........
    ...........44444445.............
    ...........4444445..............
    ..........4444445...............
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    `, SpriteKind.Player)
player3.setPosition(20, 75)
player3.setFlag(SpriteFlag.StayInScreen, true)
controller.player3.moveSprite(player3, 200, 200)
info.player3.setLife(3)
info.player3.setScore(0)
player4 = sprites.create(img`
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ....74..........................
    ....111.....999999..............
    ....4444...99999999.............
    .444.7777777999999777...........
    477.77777777777777777777........
    .44.777777777777777777777.......
    ..44.77.....777777777777........
    ...........77777777.............
    ...........7777775..............
    ..........7777775...............
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    ................................
    `, SpriteKind.Player)
player4.setPosition(20, 105)
player4.setFlag(SpriteFlag.StayInScreen, true)
controller.player4.moveSprite(player4, 200, 200)
info.player4.setLife(3)
info.player4.setScore(0)
game.onUpdateInterval(500, function () {
    if (true) {
        bogey = sprites.create(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . f . . . . . . 
            . . . . 2 2 . . f f . . . . . . 
            . . . 2 6 2 . f f f . . . . . . 
            . . 2 6 6 2 f f f f 2 5 4 4 5 . 
            2 2 2 6 6 2 f f f f 2 4 . 5 . . 
            . . 2 6 6 2 f f f f 2 5 . 4 4 5 
            . . . 2 6 2 f f f f 2 4 4 . 5 . 
            . . . . 2 2 . f f f . . . . . . 
            . . . . . . . . f f . . . . . . 
            . . . . . . . . . f . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, SpriteKind.Enemy)
        bogey.setVelocity(-50, 0)
        bogey.setPosition(180, randint(0, 120))
    } else {
    	
    }
})
