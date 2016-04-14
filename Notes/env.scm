;@ Decompose environments
(define a 5)
(println this)
(println (car this))
(println (cdr this))
;@ Check if a is a member of this
(println (member? 'a (cadr this)))
;@ prints:
;@    <environment 12409>
;@    __object
;@    ((__label __context __level __constructor this a __included_env.scm) (enviro
;@    nment <environment 3854> 0  <environment 12409> 5 #t))
;@    #t

(define (f x)
  (level 'a)
  (* x x)
)
;@ # is special keyword which gets calling env
(define (level # sym)
  (ppTable #)
)

(f 3)
;@ prints:
;@    <object 21359>
;@                     __label : environment
;@                   __context : <environment 12409>
;@                     __level : 1
;@               __constructor : <function f(x)>
;@                        this : <object 21359>
;@                           x : 3
