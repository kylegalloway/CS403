(include "exprTest.scm")
(include "streamUtils.scm")

(define (pf-3-11-17)
    (scdr
        (scons 1 (smerge
                    (smerge
                        (sscale ints 3)
                        (sscale ints 11)
                    )
                    (sscale ints 17)
                 )
        )
    )
)

(sdisplay pf-3-11-17 25)

; (define (run6)

; )