(include "extras/exprTest.scm")
(include "pretty.lib")

(define (denv id) ((get'__context) id))

(define local-ids (get 'parameters f))

()

; (define (cache x)

; )

; (define (run2)
;     (define m 2)
;     (define (msquare x) (* m x x))
;     ; (pretty msquare)
;     (define denv (get '__context msquare))
;     (ppTable denv)
;     (cache msquare)
;     ; (pretty msquare)
; )
