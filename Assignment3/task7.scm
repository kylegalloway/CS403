(include "exprTest.scm")
(include "streamUtils.scm")

(define (saverage S)
    (define (partSum)
        (psum
            (scons
                (scar S)
                (scons
                    (scar (scdr S))
                    (scons
                        (+
                            (scar S)
                            (scar (scdr S))
                        )
                        (scdr (scdr S))
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