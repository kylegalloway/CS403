(include "exprTest.scm")

(define (Queue)
    (define front (list 'head))
    (define back nil)

    (define (this msg @)
        (cond
            ((eq? msg 'enqueue) (enqueue @))
            ((eq? msg 'dequeue) (dequeue))
            ((eq? msg 'empty?) (empty?))
            (else (error "queue message not understood: " msg))
        )
    )
    (define (enqueue x) ; add to the back
        (set-cdr! back (list x))
        (set! back (cdr back))
    )

    (define (dequeue) ; remove from the front
        ; user is responsible ensuring queue is non empty
        (define tmp (cadr front))
        (set-cdr! front (cddr front))
        (if (null? (cdr front))
            (set! back front)
        )
        tmp
    )
    (define (empty?)
        (eq? (cdr front) nil)
    )

    (set! back front)
    this
)

; (inspect (define p (Queue)))
; (define p (Queue))
; (exprTest ((p 'empty?)) #t)
; (p 'enqueue 111)
; (inspect (p 'enqueue 111))
; (exprTest ((p 'empty?)) #f)
; (inspect (p 'dequeue))
; (p 'dequeue)
; (exprTest ((p 'empty?)) #t)