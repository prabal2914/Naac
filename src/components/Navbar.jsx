import React from 'react'

const Navbar = () => {
  return (
    <div>
      <div className="navbar  bg-gradient-to-r from-slate-100 to-slate-500 z-50">
  <div className="flex-1">
    <a className="btn btn-ghost normal-case text-xl">NaaC</a>
  </div>
  <div className="flex-none">
    <ul className="menu menu-horizontal px-1 text-slate-900">
      <li><a>Log in</a></li>
      <li>
        <a>Sign Up</a>
      </li>
    </ul>
  </div>
</div>
    </div>
  )
}

export default Navbar
