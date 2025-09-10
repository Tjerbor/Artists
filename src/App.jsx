function MyButton () {
  return <></>
}

export default function MyApp () {
  return (
    <>
      <div>
        <Navbar />
        {/* <SideBySide></SideBySide> */}
      </div>
    </>
  )
}

function Navbar () {
  return (
    <div className='navbar bg-neutral text-neutral-content'>
      <div className='navbar-start'>
        <div className='dropdown'>
          <div tabIndex={0} role='button' className='btn btn-ghost lg:hidden'>
            <svg
              xmlns='http://www.w3.org/2000/svg'
              className='h-5 w-5'
              fill='none'
              viewBox='0 0 24 24'
              stroke='currentColor'
            >
              {' '}
              <path
                strokeLinecap='round'
                strokeLinejoin='round'
                strokeWidth='2'
                d='M4 6h16M4 12h8m-8 6h16'
              />{' '}
            </svg>
          </div>
          <ul
            tabIndex={0}
            className='menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow'
          >
            <li>
              <NavbarRegularArtists />
            </li>
            <li>
              <NavbarNextArtist />
            </li>

            <li>
              <NavbarSideBySide />
            </li>
          </ul>
        </div>
        <a className='btn btn-ghost text-xl'>
          <strong>Real</strong> TJ Artist{' '}
          <p style={{ fontFamily: 'Rough Brush Script', fontSize: '2.1vw' }}>
            Collection
          </p>
          <b>™</b>
        </a>
      </div>
      <div className='navbar-center hidden lg:flex'>
        <ul className='menu menu-horizontal px-1'>
          <li>
            <NavbarRegularArtists />
          </li>
          <li>
            <NavbarNextArtist />
          </li>
          <li>
            <NavbarSideBySide />
          </li>
        </ul>
      </div>
      <div className='navbar-end'>
        <a className='btn'>Save</a>
      </div>
    </div>
  )
}

function NavbarRegularArtists () {
  return <a className='btn btn-ghost text-xl'>Regular Artists</a>
}

function NavbarNextArtist () {
  return <a className='btn btn-ghost text-xl'>Next Artists</a>
}
function NavbarSideBySide () {
  return <a className='btn btn-ghost text-xl'>Side by Side </a>
}

function SideBySide () {
  return (
    <div className='flex w-full'>
      <div className='card bg-base-300 rounded-box grid h-20 grow place-items-center'>
        conetnet
      </div>
      <div className='divider divider-horizontal'>OR</div>
      <div className='card bg-base-300 rounded-box grid h-20 grow place-items-center'>
        content
      </div>
    </div>
  )
}
