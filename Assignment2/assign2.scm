; Password for Submit: 16andcounting

(define (author)
    (println "AUTHOR: Kyle Galloway ckgalloway@crimson.ua.edu")
)

(define (exprTest # $expr target)
    (define result (catch (eval $expr #)))
    (if (error? result)
        (println $expr " is EXCEPTION: " (result'value)
            " (it should be " target ")")
        (println $expr " is " result
            " (it should be " target ")")
    )
)

; Task 1
(define (loop f L)
    ; If list is empty
    (if (null? L)
        ; Return null
        nil
        ; If the first part is less than the second part of the list
        (if (< (car L) (cadr L))
            (begin
                ; Call the function on the first part
                (f (car L))
                ; And recursively call loop on the rest of the sequence
                (loop f (list (+ (car L) 1) (cadr L)))
            )
        )
    )
)

; Task 2
(define (curry @)
    ; Checks if the arg is the function itself or if it is nested further down
    (if (is? (car @) 'CONS)
        ; If it is nested call the nested part L
        (define L (car @))
        ; Otherwise call the whole thing L
        (define L @)
    )
    ; Define need as the amount of parameters needed for the function in L
    (define (need) (length (get 'parameters (car L))))
    ; If length of cdr L (# of args) is less than needed
    (if (< (length (cdr L)) (need))
        ; Make a lambda that recalls the function with a more flattened list
        (lambda (@) (curry (append L @)))
        ; Else, apply the function to the rest of the list.
        (apply (car L) (cdr L))
    )
)

; Task 3
(define (infix->prefix Expr)

)

; Task 4


; Task 5

(define (fix L)
    (define (fix ly)
        (if (not (null? ly))
            (append (car ly) (list (fix (cdr ly))))
            nil
        )
    )
    (fix L)
)

(define (convert Expr)
    (define (iter exp curr)
        (if (not (null? (cdr exp)))
            (iter (cdr exp) (append curr (list (list 'lambda (list (car exp))))))
            (append curr (list (list 'lambda (list (car exp)))))
        )
    )
    (fix (append (iter (cadr Expr) '()) (list (caddr Expr))))
)

; Task 6
(define (replace-paren L)
    (define (replace-iter L newL)
        ; If L is a list
        (if (and (list? L) (not (null? L)))
            ; If (car L) is not a list
            (if (not (list? (car L)))
                ; Recur with L=>(cdr L) & newL=>(newL (car L))
                (replace-iter (cdr L)
                              (append (list (car L)) newL)
                )
                ; Else, recur with L=>(cdr L) &
                ;     newL=>(newL (replace (car L)))
                (replace-iter (cdr L) (append (replace-paren (car L)) newL))
            )
            ; Else, return (newL 'l)
            (append (list 'l) newL)
        )
    )
    ; Call replace-iter with L and ('r)
    (replace-iter L (list 'r))
)

(define (rewrite L)
    (define (rewrite-iter L newL)
        (if (and (list? L) (not (null? L)))
                  ; If (car L) is 'r
            (cond ((== (car L) 'l) (rewrite-iter (cdr L) (list newL)))
                  ; If (car L) is an integer
                  ((integer? (car L)) (rewrite-iter (cdr L) (append newL (list (car L)))))
                  (#t (rewrite-iter (cdr L) (list newL)))
            )
            newL
        )
    )
    (car (rewrite-iter L '()))
)

(define (reverse* L)
    (rewrite (replace-paren L))
)

; Task 7
(define (accumulate op initial sequence)
    (if (null? sequence)
        initial
        (op (car sequence)
            (accumulate op initial (cdr sequence))
        )
    )
)

(define (accumulate-n op init seqs)
    (if (null? (car seqs))
        nil
        (cons (accumulate op init (map car seqs))
              (accumulate-n op init (map cdr seqs))
        )
    )
)

(define (dot-product v w)
    (accumulate + 0 (map * v w))
)

(define (matrix-*-vector m v)
    (map (lambda (row) (dot-product row v)) m)
)

(define (transpose mat)
    (accumulate-n cons nil mat)
)

(define (matrix-*-matrix m n)
    (let ((cols (transpose n)))
         (map (lambda (row) (matrix-*-vector cols row)) m)
    )
)


; Task 8
(define (node value left right)
    (define (display) (print value))
    this
)

(define (displayTree root indent)
    (if (valid? root)
        (begin
            (displayTree (root'right) (string+ indent "    "))
            (print indent)
            ((root'display))
            (println)
            (displayTree (root'left) (string+ indent "    "))
        )
    )
)

(define (insertInTree root item)
    (if (>= item root'value)
        (if (null? root'right)
            ; (define (root'right) (node item nil nil))
            ; (insertInTree root'right item)
        )
        (if (null? root'left)
            ; (define (root'left) (node item nil nil))
            ; (insertInTree root'left item)
        )
    )
)

; Task 9


; Task 10


; Tests
(define (run1)
    (loop (lambda (x) (inspect x)) '(0 5))
    (loop (lambda (x) (println (* x x))) '(1 13))
    (loop (lambda (x) (println (+ x x))) '(1 11))
    (loop (lambda (x) (println (* x x x))) '(1 11))
    (loop (lambda (x) (println (+ x x x))) '(1 21))
    (loop (lambda (x) (println (sqrt x))) '(1 10))
)

(define (plus a b c d e)
      (+ a b c d e)
)
(define (run2)
    (inspect (curry plus 1 2 3 4 5))
    (inspect ((curry plus 1) 2 3 4 5))
    (inspect ((curry plus 1 2) 3 4 5))
    (inspect ((curry plus 1 2 3) 4 5))
    (inspect ((curry plus 1 2 3 4) 5))
    (inspect (((curry plus 1) 2) 3 4 5))
    (inspect (((curry plus 1) 2 3) 4 5))
    (inspect (((curry plus 1) 2 3 4) 5))
    (inspect (((((curry plus 1) 2) 3) 4) 5))
)

; (define (run3)
;     (inspect (eval (infix->prefix '(1 + 2 * 3)) this))
;     (inspect (eval (infix->prefix '(1 - 2 * 3)) this))
;     (inspect (eval (infix->prefix '(1 + 2 * 3 + 4)) this))
;     (inspect (eval (infix->prefix '(1 + 1)) this))
; )

; (define (run4))

(define (run5)
    (println (convert (quote (lambda (a b) (+ a b)))))
    (println (convert (quote (lambda (a b c) (+ a b c)))))
    (println (convert (quote (lambda (a b c d) (+ a b c d)))))
)

; (define (run6)
;     (inspect (reverse* (list 1 (list 2 (list 3  (list 4 5))))))
;     (inspect (reverse* (list 1 2 3 (list 4 5))))
;     (inspect (reverse* (list 1 (list 2 3) (list 4 5))))
;     (inspect (reverse* '(1 2 3 4 5)))
; )

; (define (run7)
;     (define v (list 1 3 -5))
;     (define w (list 4 -2 -1))
;     (inspect (dot-product v w))
;     (println "   [it should be 3]")
;     (define m (list (list 1 2 3) (list 4 5 6)))
;     (define v (list 1 2 3))
;     (inspect (matrix-*-vector m v))
;     (println "   [it should be (14 32)]")
;     (define a (list (list 14 9 3) (list 2 11 15) (list 0 12 17) (list 5 2 3)))
;     (define b (list (list 12 25) (list 9 10) (list 8 5)))
;     (inspect (matrix-*-matrix a b))
;     (println "   [it should be ((273 455) (243 235) (244 205) (102 160))]")
;     (inspect (dot-product '(0) '(0)))
;     (println "    [it should be 0]")
;     (inspect (transpose '((0))))
;     (println "    [it should be '((0))]")
;     (inspect (matrix-*-vector '((0)) '(0)))
;     (println "    [it should be '(0)]")
;     (inspect (matrix-*-matrix '((0)) '((0))))
;     (println "    [it should be '((0))]")
; )

; (define (run8)
;     (define t0 (node 5 nil nil))
;     (define t1 (insertInTree t0 2))
;     (define t2 (insertInTree t1 8))
;     (displayTree t2 "   ")
; )

; (define (run9))

; (define (run10))

; Run tests
; DONE (run1)
; DONE (run2)
; (run3)
; (run4)
; DONE (run5)
; (run6)
; (run7)
; (run8)
; (run9)
; (run10)
(println "assignment 1 loaded!")
