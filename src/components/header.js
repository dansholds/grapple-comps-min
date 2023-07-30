import React from "react";
import styled from "styled-components";
import { Link } from "gatsby";
import Container from "./container";
import ThemeSwitch from "./theme-switch";
import { useStaticQuery, graphql } from "gatsby";

const HEADER_NAV_ITEM = [
  {
    label: "Comps",
    isDropdown: true,
    dropdownOptions: [
      { label: "UK", url: "/comps" },
      { label: "US", url: "/comps-us" },
    ],
  },
  {
    label: "About",
    url: "/about",
    isExternal: false,
  },
  {
    label: "Add",
    url: "/contact",
    isExternal: false,
  },
];

const Header = () => {
  const { site } = useStaticQuery(
    graphql`
      query {
        site {
          siteMetadata {
            title
          }
        }
      }
    `
  );

  return (
    <StyledHeader>
      <HeaderWrapper>
        <HeaderTitle>
          <Link to="/">{site.siteMetadata.title}</Link>
        </HeaderTitle>

        <HeaderNavList>
          {HEADER_NAV_ITEM.map((item, index) => {
            if (item.isDropdown) {
              return (
                <HeaderNavListItem key={index}>
                  <DropdownNav label={item.label} options={item.dropdownOptions} />
                </HeaderNavListItem>
              );
            }

            if (item.isExternal) {
              return (
                <HeaderNavListItem key={index}>
                  <a href={item.url} target="_blank" rel="noopener noreferrer">
                    {item.label}
                  </a>
                </HeaderNavListItem>
              );
            }

            return (
              <HeaderNavListItem key={index}>
                <Link to={item.url}>{item.label}</Link>
              </HeaderNavListItem>
            );
          })}
          <HeaderNavListItem>
            <ThemeSwitch />
          </HeaderNavListItem>
        </HeaderNavList>
      </HeaderWrapper>
    </StyledHeader>
  );
};

export default Header;

const DropdownNav = ({ label, options }) => {
  const [isDropdownOpen, setDropdownOpen] = React.useState(false);

  const handleDropdownToggle = () => {
    setDropdownOpen(!isDropdownOpen);
  };

  const closeDropdown = () => {
    setDropdownOpen(false);
  };

  return (
    <StyledDropdownNav>
      <DropdownButton onClick={handleDropdownToggle}>
        {label} <DropdownIcon open={isDropdownOpen} />
      </DropdownButton>
      {isDropdownOpen && (
        <DropdownMenu>
          {options.map((option, index) => (
            <DropdownMenuItem key={index}>
              <Link to={option.url} onClick={closeDropdown}>
                {option.label}
              </Link>
            </DropdownMenuItem>
          ))}
        </DropdownMenu>
      )}
    </StyledDropdownNav>
  );
};

const StyledHeader = styled.header`
  padding-top: var(--size-300);
`;

const HeaderWrapper = styled(Container)`
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

const HeaderTitle = styled.div`
  & a {
    text-transform: uppercase;
    text-decoration: none;
    font-size: var(--size-400);
    color: inherit;
  }
`;

const HeaderNavList = ({ children }) => {
  return (
    <StyledNav>
      <StyledNavList>{children}</StyledNavList>
    </StyledNav>
  );
};

const HeaderNavListItem = ({ children }) => {
  return <StyledNavListItem>{children}</StyledNavListItem>;
};

const StyledNav = styled.nav`
  position: static;
  padding: 0;
  background: transparent;
  backdrop-filter: unset;
`;

const StyledNavList = styled.ul`
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 0;
  list-style-type: none;
`;

const StyledNavListItem = styled.li`
  &:not(:last-of-type) {
    margin-right: 2rem;
  }
  @media screen and (max-width: 700px) {
    &:not(:last-of-type) {
      margin-right: 1rem;
    }
  }
  & a {
    color: inherit;
    text-transform: uppercase;
    font-size: var(--size-300);
    text-decoration: none;
    letter-spacing: 0.1rem;
  }
  @media screen and (max-width: 700px) {
    & a {
      font-size: 0.7rem;
    }
  }
`;

const StyledDropdownNav = styled.div`
  position: relative;
`;

const DropdownButton = styled.button`
  background: transparent;
  border: none;
  color: inherit;
  cursor: pointer;
  text-transform: uppercase;
  font-size: var(--size-300);
  text-decoration: none;
  letter-spacing: 0.1rem;
`;

const DropdownIcon = styled.span`
  display: inline-block;
  margin-left: 0.5rem;
  transform: rotate(${(props) => (props.open ? "180deg" : "0deg")});
  transition: transform 0.2s ease;
`;

// ... (previously defined components and styles)

const DropdownMenu = styled.ul`
  position: absolute;
  top: 100%;
  left: 0;
  display: flex;
  flex-direction: column;
  padding: 0;
  list-style-type: none;
  background-color: #fff;
  border: 1px solid #ddd;
  /* Set the width of the dropdown menu to match the width of the parent nav item */
  width: 100%;

  /* Add box-shadow for a visual effect */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

  /* Optional: You can add additional styles for positioning, etc. */
  /* For example, you can position the dropdown slightly below the parent nav item */
  /* top: calc(100% + 5px); */
  /* Or align the dropdown to the right */
  /* right: 0; */
`;

const DropdownMenuItem = styled.li`
  padding: 0.5rem;
  /* No need for the border-bottom since the menu width matches the parent nav item */
  /* &:not(:last-child) {
    border-bottom: 1px solid #ddd;
  } */
  & a {
    color: inherit;
    text-decoration: none;
    /* Set the dropdown item to take up the full width */
    display: block;
    width: 100%;
  }
  & a:hover {
    color: #007bff;
    /* Optional: Add a background color on hover for better user experience */
    /* background-color: #f5f5f5; */
  }
`;
