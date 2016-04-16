(include "exprTest.scm")

(define (item v r)
    (define (dispatch m)
        (cond
            ((eq? m 'val) v)
            ((eq? m 'rank) r)
            (else (error "Unknown operation -- Item" m))
        )
    )
    dispatch
)

(define (PRQ comp)
    (define queue '())
    (define (empty? q) (= (length q) 0))
    (define pop
        (if (empty? queue)
            'EMPTY
            (car queue)
        )
    )
    (define (insert i)
        (define new (item (car i) (cdr i)))
        ; (define (iter q nitem)
        ;     (if (comp ((car q)'rank) (nitem'rank))
        ;         (iter (cdr q nitem))
        ;         (set-cdr! q (cons (car q) (cdr q)))
        ;         (set-car! q (cons new (cdr q)))
        ;     )
        ; )
        (if (empty? queue)
            (set! queue (list new))
            ; (iter queue new)
        )
    )
    (define remove
        (if (empty? queue)
            'EMPTY
            (begin
                (define p pop)
                (set! queue (cdr queue))
                p
            )
        )
    )
    (define get-value
        (if (empty? queue)
            'EMPTY
            ((car queue) 'val)
        )
    )
    (define get-rank
        (if (empty? queue)
            'EMPTY
            ((car queue) 'rank)
        )
    )

    (define (dispatch m @)
        (cond
            ((eq? m 'insert) (insert @))
            ((eq? m 'remove) (remove))
            ((eq? m 'item) get-value)
            ((eq? m 'rank) get-rank)
            ((eq? m 'size) (length queue))
            ((eq? m 'q) queue)
            ((eq? m 'empty?) (empty? queue))
            (else (error "Unknown operation -- PriorityQueue" m))
        )
    )
    dispatch
)

(inspect (define p (PRQ <)))
(inspect (p 'insert 111 0))
(exprTest (p 'size) 1)
(exprTest (p 'empty?) #f)
(exprTest (p 'item) 111)
(exprTest (p 'rank) 0)
(inspect (p 'remove))
(exprTest (p 'empty?) #t)