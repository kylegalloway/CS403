(include "extras/exprTest.scm")
(include "extras/streamUtils.scm")


(define (pf-3-11-17)
    (define S
        (scons
            1
            (smerge
                (sscale S 3)
                (smerge
                    (sscale S 11)
                    (sscale S 17)
                )
            )
        )
    )
    (scdr S)
)

(define (run6)
    (sdisplay (pf-3-11-17) 25)
)
