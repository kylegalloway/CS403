(define (cache x)

)

(define (run2)
    (define m 2)
    (define (msquare x) (* m x x))
    ; (pp msquare)
    (define denv (get '__context msquare))
    (ppTable denv)
    (cache msquare)
    ; (pp msquare)
)