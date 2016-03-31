(define (level # id)
    (this'__context)
)

; Tests
(define (f x y)
    (* (+ x y))
)

(define (run1)
    (inspect (level 'f))
)