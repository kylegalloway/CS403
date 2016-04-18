(include "extras/exprTest.scm")

(define (level # id)
    (define (env-iter env id count)
        (define in (included? id (cadr env)))
        (cond
            ((and (== in #f) (null? (get '__context env))) 'UNDEFINED)
            ((== in #t) count)
            (else
                (set! in (included? id (cadr env)))
                (env-iter (get'__context env) id (+ count 1))
            )
        )
    )
    (env-iter # id 0)
)

(define (included? x L)
    (if (null? L)
        #f
        (begin
            (if (== (car L) x)
                #t
                (included? x (cdr L))
            )
        )
    )
)

; Tests
(define a 4)

(define (f x y)
    (inspect (level 'a))
    (inspect (level 'b))
    (* (+ x y) a)
)

(define (h x y)
    (define (g)
        (inspect (level 'a))
        (inspect (level 'b))
        (* (+ x y) a)
    )
    (g)
)

(define (s)
    (define b 3)
    (lambda (x y)
        (inspect (level 'a))
        (inspect (level 'b))
        (* (+ x y) a b)
    )
)

(define (run1)
    (f 1 2)
    (h 1 2)
    ((s) 1 2)
)