; Rewrite to have book functionality with this wrapper.

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
    (define (dispatch m . args)
        (cond
            ((eq? m 'insert) (append queue (item (car args) (cadr args))))
            ((eq? m 'remove) (define pop (car queue)) (set! queue (cdr queue)))
            ((eq? m 'item) ((car queue) 'val))
            ((eq? m 'rank) ((car queue) 'rank))
            ((eq? m 'size) (length queue))
            ((eq? m 'empty?) (= (length queue) 0))
            (else (error "Unknown operation -- PriorityQueue" m))
        )
    )
    dispatch
)
