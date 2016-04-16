(include "extras/exprTest.scm")
(include "extras/streamUtils.scm")

(define (saverage S)
    (define (partSum)
        (psum
            (scons
                (scar S)
                (scons
                    (scadr S)
                    (scons
                        (+
                            (scar S)
                            (scadr S)
                        )
                        (scddr S)
                    )
                )
            )
        )
    )
    (div-streams (partSum) (floats-from 1))
)

(define (run7)
    (sdisplay (saverage ints) 10)
    (sdisplay (saverage odds) 10)
    (sdisplay (saverage evens) 10)
    (sdisplay (saverage alt-ones) 10)
)