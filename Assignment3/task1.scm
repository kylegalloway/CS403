(define (level # id)
    (inspect (cadr (get'__context)))
    (inspect (caddr (get'__context)))
)

; Tests
(define a 4)
(define (f x y)
    (level 'a)
    (* (+ x y) a)

)

(f 1 2)
; (define (run1)
; )