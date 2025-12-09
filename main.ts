input.onButtonPressed(Button.A, function () {
    hand = hand + 1
    if (hand > 3) {
        hand = 1
    }
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.Scissors)
        music.play(music.createSoundExpression(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    }
})
input.onGesture(Gesture.Shake, function () {
    handCPU = randint(1, 3)
    if (handCPU == 1) {
        basic.showIcon(IconNames.SmallSquare)
        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    } else if (handCPU == 2) {
        basic.showIcon(IconNames.Square)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.Scissors)
        music.play(music.createSoundExpression(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    }
})
input.onButtonPressed(Button.B, function () {
    handCPU = randint(1, 3)
    basic.showString("CPU")
    if (handCPU == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (handCPU == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    basic.showString("YOU")
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    if (hand == 1) {
        if (handCPU == 2) {
            basic.showString("LOSE")
        } else if (handCPU == 3) {
            basic.showString("WIN")
        } else {
            basic.showString("DRAW")
        }
    } else if (hand == 2) {
        if (handCPU == 1) {
            basic.showString("WIN")
        } else if (handCPU == 3) {
            basic.showString("LOSE")
        } else {
            basic.showString("DRAW")
        }
    } else {
        if (handCPU == 1) {
            basic.showString("LOSE")
        } else if (handCPU == 2) {
            basic.showString("WIN")
        } else {
            basic.showString("DRAW")
        }
    }
})
let handCPU = 0
let hand = 0
hand = 0
basic.showString("CPU vs YOU")
basic.forever(function () {
	
})
