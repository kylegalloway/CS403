(include "extras/exprTest.scm")

(define (denv # id) ((get'__context) id))

(define listofsymbols '(+ - * / ^))

; (println (denv (car listofsymbols)))

; (define (cache x)

; )

; (define (run2)
;     (define m 2)
;     (define (msquare x) (* m x x))
;     ; (pp msquare)
;     (define denv (get '__context msquare))
;     (ppTable denv)
;     (cache msquare)
;     ; (pp msquare)
; )
